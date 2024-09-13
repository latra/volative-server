from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from database import Base


class Voice(Base):
    __tablename__ = 'voice'
    
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    voice_name = Column(String, nullable=False)
    samples_path = Column(String, nullable=False)
    
    project_uuid = Column(UUID(as_uuid=True), ForeignKey('project.uuid'))
    jobs = relationship('Job', back_populates='voice')
    project = relationship('Project', back_populates='voices')
