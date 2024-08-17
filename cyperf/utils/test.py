import cyperf
import urllib3
import requests
from cyperf.rest import ApiException
from pprint import pprint

import time

class TestConfig(object):
    def __init__(self, configFile, agentMapping, objectiveType, objectiveValue, verifyRules):
        self.file      = configFile
        self.agents    = agentMapping
        self.objective = {
            'type'  : objectiveType,
            'value' : objectiveValue
        }
        self.statRules = []

class TestRunner(object):
    WAP_CLIENT_ID = 'clt-wap'

    def __init__(self, controller, username, password):
        self.host        = f'https://{controller}'
        self.username    = username
        self.password    = password

        self.configuration = cyperf.Configuration(host = self.host)
        self.configuration.access_token = self.__authorize__()
        self.configuration.verify_ssl   = False
        self.apiClient     = cyperf.ApiClient(self.configuration)

    def __authorize__(self):
        session = requests.Session()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        session.verify = False

        url     = f'{self.host}/auth/realms/keysight/protocol/openid-connect/token'
        headers = {"content-type" : "application/x-www-form-urlencoded"}
        payload = {"username"     : self.username,
                   "password"     : self.password,
                   "grant_type"   : "password",
                   "client_id"    : TestRunner.WAP_CLIENT_ID}
        response = session.post(url, headers = headers, data = payload, verify = False)
        if response.headers.get('content-type') == 'application/json':
            return response.json()['access_token']
        else:
            raise Exception(f'Cannot generate access token for {self.host}')

    def Authorize(self):
        self.configuration.access_token = self.__authorize__()

    def LoadConfigs(self, configFiles):
        apiInstance = cyperf.ConfigurationsApi(self.apiClient)
        results     = []
        for cFile in configFiles:
            response = apiInstance.api_v2_configs_operations_import_post (cFile)
            while 'IN_PROGRESS' == response.state:
                response = apiInstance.api_v2_configs_operations_import_id_get(response.id)
            if 'SUCCESS' == response.state:
                results += response.result

        return [cyperf.AppsecConfig.from_dict(e['configData']) for e in results]

    def DeleteConfig(self, configs):
        apiInstance = cyperf.ConfigurationsApi(self.apiClient)
        for config in configs:
            apiInstance.api_v2_configs_config_id_delete (config.id)

    def Run(self, config):
        pprint (f"Loading configuration {config.file} ...")
        configs = self.LoadConfigs ([config.file])
        pprint (f"Loaded configuration {config.file} ...")
        time.sleep(10)
        pprint (f"Deleting configuration {config.file} ...")
        self.DeleteConfig (configs)
        pprint (f"Deleted configuration {config.file} ...")

