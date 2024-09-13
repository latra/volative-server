from sqlalchemy import insert, Sequence, Row, select, and_

from repository.base import BaseRepository
from models import User, user_project_role
from sqlalchemy.orm import Session
from schemas import UserResponse
from exceptions import username_exists, email_exists
class UserRepository(BaseRepository):
    def register_user(self, session: Session, user: User) -> User:
        exist_user = self.get_by_username(session, user.username)
        if exist_user:
            raise username_exists
        exist_user = self.get_by_email(session, user.email)
        if exist_user:
            raise email_exists
        user = self.add(session, user)
        return user

    def get_by_username(self, session: Session, username) -> User:
        return self.get(session, User, query= User.username==username)
    
    def get_by_email(self, session: Session, email) -> User:
        return self.get(session, User, query= User.email==email)

    def get_by_uuid(self, session: Session, uuid) -> User:
        return self.get(session, User, query= User.uuid==uuid)

    def get_user_in_project(self, session: Session, project_uuid, user_uuid) -> User:
        stmt = select(User, user_project_role.c.role).join(
                    user_project_role, user_project_role.c.user_uuid == User.uuid
                ).where(and_(user_project_role.c.project_uuid == project_uuid, user_project_role.c.user_uuid == user_uuid))
                
        result = session.execute(stmt).first()
        return result
