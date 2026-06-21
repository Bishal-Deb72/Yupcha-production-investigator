import re



def parse_logs(logs:str):


    timestamps=[]
    errors=[]
    deployments=[]
    services=[]



    lines=logs.split("\n")



    for line in lines:


        timestamp_match=re.search(

            r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',
            line

        )


        if timestamp_match:

            timestamps.append(

                timestamp_match.group()

            )



        if "ERROR" in line:

            errors.append(line)



        if "deploy" in line.lower():

            deployments.append(line)



        service_match=re.search(

            r'([A-Za-z]+)\sService',

            line

        )


        if service_match:

            services.append(

                service_match.group(1)

            )



    return {

        "timestamps":list(set(timestamps)),

        "errors":list(set(errors)),

        "deployments":list(set(deployments)),

        "services":list(set(services))
    }