from pydantic import BaseModel, UUID4

class JobBase(BaseModel):
    status: str
    text: str

class JobCreate(JobBase):
    work_batch_uuid: UUID4
    voice_uuid: UUID4

class JobUpdate(JobBase):
    pass

class JobResponse(JobBase):
    uuid: UUID4

    class Config:
        orm_mode = True
