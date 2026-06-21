from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime

from app.core.database import Base


class Incident(Base):

    __tablename__="incidents"


    id=Column(Integer,primary_key=True,index=True)

    title=Column(String)

    logs=Column(Text)

    stack_trace=Column(Text)

    deployment_history=Column(Text)

    parsed_data = Column(Text)
    timeline = Column(Text)
    hypotheses=Column(Text)

    root_cause=Column(Text)

    recommendations=Column(Text)

    confidence_score=Column(Integer)

    status=Column(String,default="uploaded")



    created_at=Column(
                    DateTime,
                    default=datetime.utcnow
                    )