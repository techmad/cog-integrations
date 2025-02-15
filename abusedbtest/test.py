
import json
import requests
from . import config

def print():
    configs = config.yaml2dict()
    return configs

def integration(instance: dict, params: dict, config = { "timeout" : 15 }):

    #print(configs)

    #url = instance["url"] 

    commands = ['ip',
                'check_ip_command',
                'check-cidr-block',
                'report-ip',
                'blacklist',
                'get-categories'
                ]
  
    #with open('config.yml', 'r') as file:
    #    config = yaml.safe_load(file)


    try:
        #response = requests.post(url, data=params, timeout=config['timeout'])
        #json_response = response.content.decode("utf-8", "ignore")
        #json_response = json.loads(json_response)['data']
        return {
                "status": "OK",
                #"response" : json_response,
                #"test": config,
                "type" : "list-objects"
            }
    
    except Exception as e:
        return {"status": "ERROR",
                 "response" : str(e)
        }
