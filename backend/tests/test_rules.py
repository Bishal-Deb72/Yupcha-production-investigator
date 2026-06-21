from app.services.rules import generate_hypotheses



sample = {

    "errors":[

        "ERROR Database Connection Timeout",

        "ERROR Redis unavailable"

    ],


    "deployments":[

        "Deployment v2.3 completed"

    ]

}



result = generate_hypotheses(sample)



print(result)