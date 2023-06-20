import uvicorn
from fastapi import FastAPI

from src.apis.address.routers import address_router
from src.settings.database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(address_router)

if __name__ == "__main__":
    uvicorn.run("app:app")
