import requests
import json
import yaml

def integration(instance, params, config = { "timeout" : 15 }):

    url = instance["url"] # "https://mb-api.abuse.ch/api/v1/") 

    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)

    try:
        response = requests.post(url, data=params, timeout=config['timeout'])

        json_response = response.content.decode("utf-8", "ignore")
        json_response = json.loads(json_response)['data']
        return {"status": "OK",
                 "response" : json_response,
                 "config" : config,
                 "type" : "list-objects"
        }
    
    except Exception as e:
        return {"status": "ERROR",
                 "response" : str(e)
        }
