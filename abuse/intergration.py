import requests
import json

def integration(instance, params, config = { "timeout" : 15 }):

    url = instance["url"] # "https://mb-api.abuse.ch/api/v1/") 

    try:
        response = requests.post(url, data=params, timeout=config['timeout'])

        json_response = response.content.decode("utf-8", "ignore")
        json_response = json.loads(json_response)['data']
        return {"status": "OK",
                 "response" : json_response,
                 "type" : "list-objects"
        }
    
    except Exception as e:
        return {"status": "ERROR",
                 "response" : str(e)
        }
