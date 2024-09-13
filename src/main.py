from fastapi import FastAPI
from routers import api_router
from database import engine, Base

app = FastAPI()

app.include_router(api_router)

@app.on_event("startup")
async def setup():
    Base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Events API"}
