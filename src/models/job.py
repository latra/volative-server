from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from database import Base

class Job(Base):
    __tablename__ = 'job'
    
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status = Column(String, nullable=False)
    text = Column(String, nullable=False)
    
    # Clave foránea que apunta a WorkBatch
    work_batch_uuid = Column(UUID(as_uuid=True), ForeignKey('work_batch.uuid'))
    
    # Clave foránea que apunta a Voice
    voice_uuid = Column(UUID(as_uuid=True), ForeignKey('voice.uuid'))
    
    # Relación uno a uno con Audio
    audio = relationship('Audio', uselist=False, back_populates='job')
    
    # Relación inversa con WorkBatch y Voice
    work_batch = relationship('WorkBatch', back_populates='jobs')
    voice = relationship('Voice', back_populates='jobs')