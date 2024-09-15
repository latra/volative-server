from pydantic import BaseModel
from enums import Roles
from schemas.user import UserResponse
from schemas.project import ProjectResponse

class UserRoleBase(BaseModel):
    user_uuid: str
    project_uuid: str

class UserRoleCreate(UserRoleBase):
    role: Roles


class UserRoleResponse(UserRoleBase):
    user: UserResponse
    project: ProjectResponse