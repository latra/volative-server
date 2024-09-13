from sqlalchemy import Column, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from database import Base

user_project_role = Table('user_project_role', Base.metadata,
    Column('user_uuid', UUID(as_uuid=True), ForeignKey('user.uuid'), primary_key=True),
    Column('project_uuid', UUID(as_uuid=True), ForeignKey('project.uuid'), primary_key=True),
    Column('role', String, nullable=False)
)

class User(Base):
    __tablename__ = 'user'
    
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_admin = Column(Boolean, default=False)
    
    # Relación muchos a muchos con Project a través de UserProjectRole
    projects = relationship('Project', secondary=user_project_role, back_populates='users')