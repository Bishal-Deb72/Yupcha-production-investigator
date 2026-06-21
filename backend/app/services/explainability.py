def explain(parsed, timeline, hypotheses):


    return {

        "errors_found":
        parsed["errors"],


        "deployment_events":
        parsed["deployments"],


        "services":
        parsed["services"],


        "hypotheses_used":
        hypotheses,


        "timeline_events":
        timeline
    }