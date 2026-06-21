import os
import json

from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)



def analyze_incident(

        parsed,
        timeline,
        hypotheses
):



    prompt=f"""


You are a Senior Site Reliability Engineer.



Parsed Data:

{parsed}



Timeline:

{timeline}




Hypotheses:

{hypotheses}




Return JSON only.



Format:



{{

"summary":"",

"root_cause":"",

"confidence":0,

"recommendations":[]

}}

"""




    response=model.generate_content(
        prompt
    )




    try:



        result=response.text


        result=result.replace(
            "```json",
            ""
        )


        result=result.replace(
            "```",
            ""
        )



        return json.loads(result)



    except Exception:



        return {


            "summary":"Analysis failed",


            "root_cause":"Unknown",


            "confidence":0,


            "recommendations":[

                "Review logs manually"

            ]
        }