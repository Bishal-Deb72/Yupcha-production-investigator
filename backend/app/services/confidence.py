def confidence_score(

        parsed,

        hypotheses

):



    score=40



    if parsed["errors"]:
        score+=20



    if parsed["deployments"]:
        score+=20



    if len(hypotheses)>1:
        score+=20



    return min(score,100)