def generate_hypotheses(parsed_data):

    hypotheses = []

    errors = parsed_data.get("errors", [])
    deployments = parsed_data.get("deployments", [])



    if deployments:
        hypotheses.append(
            "Recent deployment may have introduced regression"
        )



    for error in errors:

        lower = error.lower()


        if "database" in lower:

            hypotheses.append(
                "Database connectivity issue detected"
            )


        elif "redis" in lower:

            hypotheses.append(
                "Redis service may be unavailable"
            )


        elif "timeout" in lower:

            hypotheses.append(
                "Service timeout detected"
            )


        elif "memory" in lower:

            hypotheses.append(
                "Possible memory exhaustion"
            )


        elif "cpu" in lower:

            hypotheses.append(
                "High CPU usage suspected"
            )


    return list(set(hypotheses))