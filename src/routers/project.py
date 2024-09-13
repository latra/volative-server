from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from enums import Roles
import schemas, models, services.auth as auth
from database import get_db
from dependencies import get_current_user, get_current_admin_user
from schemas import User, UserRoleCreate
from repository import ProjectRepository, UserRepository
from exceptions import missing_query_parameters, incopatible_query_parameters, project_not_found, permission_exception, user_not_found, user_exists_at_project
project_router = APIRouter()
project_repository = ProjectRepository()
user_repository = UserRepository()

def user_is_mod(db:  Session, user: User, project_uuid: str) -> bool:
    if user.is_admin:
        return True
    result = user_repository.get_user_in_project(db, project_uuid, user.uuid)
    if result and result[0] and result[1] == Roles.MODERATOR:
        return True
    return False


@project_router.post("/", response_model=schemas.ProjectResponse)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db), admin_user: User = Depends(get_current_admin_user)):
    db_project = models.Project(name=project.name, description=project.description)
    project = project_repository.register_project(db, db_project)
    return schemas.ProjectResponse.model_validate(project)

@project_router.post("/register", response_model=schemas.ProjectResponse)
def register_user(register_request: UserRoleCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if not user_is_mod(db, user, register_request.project_uuid):
        raise permission_exception
    project = project_repository.get_project_by_uuid(db, register_request.project_uuid)
    if not project:
        raise project_not_found
    
    user_to_add = user_repository.get_by_uuid(db, register_request.user_uuid)
    if not user_to_add:
        raise user_not_found
    
    relation_exists = user_repository.get_user_in_project(db, register_request.project_uuid, register_request.user_uuid)
    if relation_exists and relation_exists[1] == register_request.role:
        raise user_exists_at_project
    
    if relation_exists and relation_exists[1] == Roles.MODERATOR and not user.is_admin:
        raise permission_exception
    
    if relation_exists:
        project_repository.update_user_to_project(db, register_request.project_uuid, register_request.user_uuid, register_request.role)
    else:
        project_repository.register_user_to_project(db, register_request.project_uuid, register_request.user_uuid, register_request.role)

    project_response = schemas.ProjectResponse.model_validate(project)
    users = project_repository.get_users_from_project(db, project.uuid)
    project_response.load_users(users)
    return project_response

@project_router.get("/", response_model=schemas.ProjectResponse)
def register_user(name: str = None, uuid: str = None, load_users: bool = False, db: Session = Depends(get_db)):
    if name is None and uuid is None:
        raise missing_query_parameters
    elif name and uuid:
        raise incopatible_query_parameters
    
    if name:
        project = project_repository.get_project_by_name(db, name)
    else:
        project = project_repository.get_project_by_uuid(db, uuid)
    
    if not project:
        raise project_not_found
    
    
    project_response = schemas.ProjectResponse.model_validate(project)
    if load_users:
        users = project_repository.get_users_from_project(db, project.uuid)
        project_response.load_users(users)
    return project_response