import json
from fastapi import APIRouter
from fastapi import Depends
from app.services.parser import parse_logs
from app.services.timeline import reconstruct_timeline
from app.services.rules import generate_hypotheses
from app.services.parser import parse_logs
from app.services.analyzer import analyze_incident
from app.services.explainability import explain
from app.services.confidence import confidence_score
from app.services.parser import parse_logs
from app.services.timeline import reconstruct_timeline
from app.services.rules import generate_hypotheses
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.incident import Incident
from app.schemas.incident import (
        IncidentCreate,
        IncidentResponse
)

router=APIRouter()

@router.post("/incidents")


def create_incident(

        data:IncidentCreate,

        db:Session=Depends(get_db)

):



    incident=Incident(

            title=data.title,

            logs=data.logs,

            stack_trace=data.stack_trace,

            deployment_history=data.deployment_history

    )



    db.add(incident)

    db.commit()

    db.refresh(incident)



    return incident

@router.get("/incidents")


def get_incidents(

        db:Session=Depends(get_db)

):



    return db.query(Incident).all()

@router.post("/parse")


def parse(data:dict):


    logs=data["logs"]


    result=parse_logs(logs)



    return result

@router.post("/timeline")

def timeline(data: dict):

    logs = data["logs"]

    result = reconstruct_timeline(logs)

    return result


@router.post("/hypotheses")

def hypotheses(data: dict):


    logs = data["logs"]


    parsed = parse_logs(logs)



    result = generate_hypotheses(parsed)



    return {

        "hypotheses": result
    }


@router.post("/analyze")


def analyze(data:dict, db:Session=Depends(get_db)):



    logs = data["logs"]

    incident=Incident(

        title="Generated Incident",

        logs=logs

    )



    db.add(incident)


    db.commit()


    db.refresh(incident)

    parsed = parse_logs(logs)



    timeline = reconstruct_timeline(logs)



    hypotheses = generate_hypotheses(parsed)




    analysis  = analyze_incident(

            parsed,

            timeline,

            hypotheses
    )

    explanation = explain(

        parsed,

        timeline,

        hypotheses
    )
    confidence = confidence_score(

        parsed,

        hypotheses
    )

    incident.root_cause = analysis["root_cause"]


    incident.confidence_score = confidence


    incident.timeline = json.dumps(
            timeline
    )


    incident.parsed_data = json.dumps(
            parsed
    )


    incident.hypotheses = json.dumps(
            hypotheses
    )


    incident.recommendations = json.dumps(

            analysis["recommendations"]

    )


    db.commit()


    return{


    "analysis":analysis,


    "confidence":confidence,


    "explainability":explanation


}