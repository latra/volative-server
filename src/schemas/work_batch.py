from pydantic import BaseModel, UUID4
from typing import Optional

class WorkBatchBase(BaseModel):
    description: Optional[str] = None
    model: str

class WorkBatchCreate(WorkBatchBase):
    project_uuid: UUID4

class WorkBatchUpdate(WorkBatchBase):
    pass

class WorkBatchResponse(WorkBatchBase):
    uuid: UUID4

    class Config:
        orm_mode = True
