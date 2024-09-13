from pydantic import BaseModel, UUID4
from typing import Optional
from schemas.user import UserResponse 
from enums import Roles
from sqlalchemy import Sequence, Row
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass


class ProjectResponse(ProjectBase):
    uuid: UUID4
    moderators: Optional[list[UserResponse]] = None
    collaborators: Optional[list[UserResponse]] = None
    class Config:
        from_attributes = True

    def load_users(self, list_users: Sequence[Row]):
        self.moderators = []
        self.collaborators = []
        for user, role in list_users:
            user_response = UserResponse.model_validate(user)
            if role == Roles.MODERATOR:
                self.moderators.append(user_response)
            elif role == Roles.COLLABORATOR:
                self.collaborators.append(user_response)
