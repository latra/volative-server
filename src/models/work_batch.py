from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from database import Base


class WorkBatch(Base):
    __tablename__ = 'work_batch'
    
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    description = Column(String)
    model = Column(String)
    
    project_uuid = Column(UUID(as_uuid=True), ForeignKey('project.uuid'))
    jobs = relationship('Job', back_populates='work_batch')
    project = relationship('Project', back_populates='work_batches')