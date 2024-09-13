from pydantic import BaseModel, UUID4

class VoiceBase(BaseModel):
    voice_name: str
    samples_path: str

class VoiceCreate(VoiceBase):
    project_uuid: UUID4

class VoiceUpdate(VoiceBase):
    pass

class VoiceResponse(VoiceBase):
    uuid: UUID4

    class Config:
        orm_mode = True
