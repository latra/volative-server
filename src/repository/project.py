from sqlalchemy import insert, Sequence, Row, select, and_, update

from repository.base import BaseRepository
from models import Project, user_project_role, User
from sqlalchemy.orm import Session
from schemas import ProjectResponse
from exceptions import project_name_in_use, project_not_found
class ProjectRepository(BaseRepository):
    def register_project(self, session: Session, project: Project) -> Project:
        exist_project = self.get_project_by_name(session, project.name)
        if exist_project:
            raise project_name_in_use
        project = self.add(session, project)
        return project
    
    def get_project_by_name(self, session: Session, project_name) -> Project:
        exist_project = self.get(session, Project, query = Project.name==project_name)
        return exist_project
    
    def get_project_by_uuid(self, session: Session, project_uuid) -> Project:
        exist_project = self.get(session, Project, query = Project.uuid==project_uuid)
        return exist_project
    
    def get_users_from_project(self, session: Session, project_uuid) -> Sequence[Row]:
        stmt = select(User, user_project_role.c.role).join(
                    user_project_role, user_project_role.c.user_uuid == User.uuid
                ).where(user_project_role.c.project_uuid == project_uuid)
                
        result = session.execute(stmt).all()
        return result

    def register_user_to_project(self, session: Session, project_uuid, user_uuid, role) -> None:
        session.execute(insert(user_project_role).values(
            user_uuid=user_uuid, project_uuid=project_uuid, role=role
        ))
        session.commit()
    
    def update_user_to_project(self, session: Session, project_uuid, user_uuid, new_role) -> None:
        stmt = (
            update(user_project_role)
            .where(
                user_project_role.c.user_uuid == user_uuid,
                user_project_role.c.project_uuid == project_uuid
            )
            .values(role=new_role) 
        )

        session.execute(stmt)
        session.commit()
