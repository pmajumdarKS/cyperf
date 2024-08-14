import cyperf
import urllib3
import requests
from cyperf.rest import ApiException
from pprint import pprint

class TestConfig(object):
    def __init__(self, configFile, agentMapping, objectiveType, objectiveValue, verifyRules):
        self.config    = configFile
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
        self.apiClient     = cyperf.ApiClient(configuration)

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

    def authorize(self):
        self.configuration.access_token = self.__authorize__()

    def run(self, config):
        pass

runner = TestRunner ('10.36.75.241', 'admin', 'CyPerf&Keysight#1')
print(runner.configuration.access_token)
