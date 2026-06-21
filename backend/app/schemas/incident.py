from pydantic import BaseModel


class IncidentCreate(BaseModel):


    title:str


    logs:str


    stack_trace:str


    deployment_history:str





class IncidentResponse(IncidentCreate):


    id:int


    status:str



    class Config:

        from_attributes=True