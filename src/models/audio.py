from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from database import Base

class Audio(Base):
    __tablename__ = 'audio'
    
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    path = Column(String, nullable=False)
    length = Column(Integer)
    
    # Clave foránea que apunta a Job
    job_uuid = Column(UUID(as_uuid=True), ForeignKey('job.uuid'))
    
    # Relación inversa con Job
    job = relationship('Job', back_populates='audio')
