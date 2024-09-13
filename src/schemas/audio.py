from pydantic import BaseModel, UUID4

class AudioBase(BaseModel):
    path: str
    length: int

class AudioCreate(AudioBase):
    job_uuid: UUID4

class AudioUpdate(AudioBase):
    pass

class AudioResponse(AudioBase):
    uuid: UUID4

    class Config:
        orm_mode = True
