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
        self.agents        = {}

        self.RefreshAgents()

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
        response = session.post(url, headers = headers, data = payload, verify = False, timeout = (10, 30))
        if response.headers.get('content-type') == 'application/json':
            return response.json()['access_token']
        else:
            raise Exception(f'Cannot generate access token for {self.host}')

    def Authorize(self):
        self.configuration.access_token = self.__authorize__()

    def RefreshAgents(self):
        apiInstance = cyperf.AgentsApi(self.apiClient)
        try:
            response = apiInstance.api_v2_agents_get() ## This is an object instead of a json
            agents   = response.actual_instance
            for agent in agents:
                self.agents [agent.ip] = agent
            pprint (self.agents)
        except cyperf.exceptions.ApiException as e:
            pprint (e)

    def LoadConfigs(self, configFiles):
        apiInstance = cyperf.ConfigurationsApi(self.apiClient)
        results     = []
        for cFile in configFiles:
            response = apiInstance.api_v2_configs_operations_import_post (cFile)
            while 'IN_PROGRESS' == response.state:
                response = apiInstance.api_v2_configs_operations_import_id_get(response.id)
            if 'SUCCESS' == response.state:
                results += response.result

        #pprint(results)
        # Why isn't configUrl a part of AppsecConfig?
        configs = {}
        for e in results:
            configs [e['id']] = (e['configUrl'], cyperf.AppsecConfig.from_dict(e['configData']))
        return configs

    def DeleteConfig(self, configs):
        apiInstance = cyperf.ConfigurationsApi(self.apiClient)
        for configUrl, config in configs.values():
            apiInstance.api_v2_configs_config_id_delete (config.id)

    def LaunchSessions(self, configs):
        apiInstance = cyperf.SessionsApi(self.apiClient)
        sessions    = []
        for configUrl, config in configs.values():
            session = cyperf.Session()
            session.config     = config
            session.config_url = configUrl
            sessions.append (session)
        try:
            sessions = apiInstance.api_v2_sessions_post(session=sessions)
            for session in sessions:
                session.config = configs[session.config_url][1]
            return sessions
        except cyperf.exceptions.ApiException as e:
            pprint (e)
            return []

    def CloseSessions(self, sessions):
        apiInstance = cyperf.SessionsApi(self.apiClient)
        for session in sessions:
            try:
                apiInstance.api_v2_sessions_session_id_delete (session.id)
            except cyperf.exceptions.ApiException as e:
                pprint (e)

    def __updateAgents__(self, session, agentMapping):
        config      = session.config.config
        netProfiles = config.network_profiles
        for netProfile in netProfiles:
            ipNets = netProfile.ip_network_segment
            for ipNet in ipNets:
                if ipNet.name in agentMapping:
                    pprint (f"Found an agent for {ipNet.name} with ip {agentMapping[ipNet.name]}")
                    if not ipNet.agent_assignments:
                        ipNet.agent_assignments = cyperf.AgentAssignments()
                    agents = agentMapping[ipNet.name]
                    for agentName in agents:
                        if agentName in self.agents:
                            agent = self.agents[agentName]
                            interfaces = [iFace.name for iFace in agent.interfaces]
                            agentDetails = cyperf.AgentAssignmentDetails(agent_id = agent.id, id = agent.id, interfaces = interfaces)
                            ipNet.agent_assignments.by_id.append(agentDetails)
                        else:
                            pprint (f'Could not find the agent {agentName} in the registered list')
        apiInstance = cyperf.SessionsApi(self.apiClient)
        #try:
        #    session.config = apiInstance.api_v2_sessions_session_id_config_put(session.id, session.config)
        #    pprint (session)
        #except cyperf.exceptions.ApiException as e:
        #    pprint (e)

    def UpdateAgents(self, sessions, agentMapping):
        for session in sessions:
            self.__updateAgents__(session, agentMapping)

    def Run(self, config):
        width = 200
        pprint (f"Loading configuration {config.file} ...", width=width)
        configs  = self.LoadConfigs ([config.file])
        pprint (f"Launching session for configuration {config.file} ...", width=width)
        sessions = self.LaunchSessions (configs)
        pprint (f"Updating agents as {config.agents} ...", width=width)
        self.UpdateAgents (sessions, config.agents)
        pprint (f"Started test for configuration {config.file} ... session id: {sessions[0].index}", width=width)
        time.sleep(10)
        pprint (f"Closing session for configuration {config.file} ...", width=width)
        self.CloseSessions (sessions)
        pprint (f"Deleting configuration {config.file} ...", width=width)
        self.DeleteConfig (configs)
        pprint (f"Deleted configuration {config.file} ...", width=width)

