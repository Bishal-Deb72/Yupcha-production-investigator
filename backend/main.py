from fastapi import FastAPI

from app.core.database import Base
from app.core.database import engine

from app.routers.incidents import router


Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="Yupcha Incident Investigator"
)




@app.get("/")


def home():

    return {
        "message":"Running"
    }

app.include_router(router)