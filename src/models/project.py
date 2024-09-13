from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from models.user import user_project_role
from database import Base


class Project(Base):
    __tablename__ = 'project'
    
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)
    users = relationship('User', secondary=user_project_role, back_populates='projects')
    work_batches = relationship('WorkBatch', back_populates='project')
    voices = relationship('Voice', back_populates='project')
