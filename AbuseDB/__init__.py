
import json
import requests
import yaml


def integration(instance: dict, params: dict, config : dict = { "timeout" : 15 }):

    url = instance["url"] 

    commands = ['ip',
                'check_ip_command',
                'check-cidr-block',
                'report-ip',
                'blacklist',
                'get-categories'
                ]
  


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

    try:
        reliability = demisto.params().get('integrationReliability', 'C - Fairly reliable')

        if DBotScoreReliability.is_valid_type(reliability):
            reliability = DBotScoreReliability.get_dbot_score_reliability_from_str(reliability)
        else:
            raise Exception("Please provide a valid value for the Source Reliability parameter.")

        if command == 'test-module':
            # Tests connectivity and credentails on login
            test_module(reliability)
        elif command == 'ip':
            demisto.results(check_ip_command(reliability, **demisto.args()))
        elif demisto.command() == 'check-cidr-block':
            demisto.results(check_block_command(reliability, **demisto.args()))
        elif command == 'report-ip':
            demisto.results(report_ip_command(**demisto.args()))
        elif command == 'blacklist':
            demisto.results(get_blacklist_command(**demisto.args()))
        elif command == 'get-categories':
            demisto.results(get_categories_command(**demisto.args()))  # type:ignore

    except Exception as e:
        return_error(str(e))

def http_request(method, url_suffix, params=None, headers=HEADERS, threshold=THRESHOLD):


    try:
        analysis = session.request(method, SERVER + url_suffix, headers=headers, params=params, verify=not INSECURE)

        if analysis.status_code not in {200, 204, 429}:
            return_error('Bad connection attempt. Status code: ' + str(analysis.status_code))
        if analysis.status_code == 429:
            if demisto.params().get('disregard_quota'):
                return API_QUOTA_REACHED_MESSAGE
            else:
                return_error(API_QUOTA_REACHED_MESSAGE)

        return REPORT_SUCCESS if url_suffix == REPORT_CMD else analysis.json()
    except Exception as e:
        LOG(e)
        return_error(str(e))
