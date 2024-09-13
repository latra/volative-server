from pydantic import BaseModel
from enums import Roles
from schemas.user import UserResponse
from schemas.project import ProjectResponse

class UserRoleBase(BaseModel):
    role: Roles

class UserRoleCreate(UserRoleBase):
    user_uuid: str
    project_uuid: str

class UserRoleResponse(UserRoleBase):
    user: UserResponse
    project: ProjectResponse