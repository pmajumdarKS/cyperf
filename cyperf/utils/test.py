import cyperf
import re
import urllib3
import requests
from cyperf.rest import ApiException
from pprint import pprint

import time

class TestConfig(object):
    def __init__(self,
                 configFile,
                 agentMapping={},
                 objectiveType=cyperf.ObjectiveType.SIMULATED_USERS,
                 objectiveValue=100,
                 testDuration=0,
                 verifyRules=None):
        objectiveUnit = None
        if type(objectiveValue) == str:
            val = re.compile('(\d+\.\d+|\d+)\s*(\w*)').match(objectiveValue).groups()
            objectiveValue = float(val[0])
            if val[1]:
                objectiveUnit = val[1]

        if not objectiveUnit:
            if objectiveType == cyperf.ObjectiveType.THROUGHPUT:
                objectiveUnit = 'bps'
            else:
                objectiveUnit = ''

        self.file      = configFile
        self.agents    = agentMapping
        self.duration  = testDuration
        self.objective = {
            'type'  : objectiveType,
            'value' : objectiveValue,
            'unit'  : objectiveUnit
        }
        self.statRules = []

class TestRunner(object):
    WAP_CLIENT_ID = 'clt-wap'

    def __init__(self, controller, username="", password="", refresh_token="", licenseServer = None):
        self.host          = f'https://{controller}'
        self.username      = username
        self.password      = password
        self.refresh_token = refresh_token
        self.licenseServer = licenseServer
        self.configuration = cyperf.Configuration(host = self.host)
        self.configuration.verify_ssl   = False
        self.apiClient     = cyperf.ApiClient(self.configuration)
        self.agents        = {}

        self.configuration.access_token = self.__authorize__()

        self.UpdateLicenseServer()
        self.RefreshAgents()

    def __authorize__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        apiInstance = cyperf.AuthorizationApi(self.apiClient)
        grant_type = "refresh_token" if self.refresh_token else "password"
        try:
            response = apiInstance.auth_realms_keysight_protocol_openid_connect_token_post (client_id  = TestRunner.WAP_CLIENT_ID,
                                                                                            grant_type = grant_type,
                                                                                            password   = self.password,
                                                                                            username   = self.username,
                                                                                            refresh_token = self.refresh_token)
            return response.access_token
        except cyperf.exceptions.ApiException as e:
            raise (e)

    def Authorize(self):
        self.configuration.access_token = self.__authorize__()

    def UpdateLicenseServer (self):
        if not self.licenseServer:
            return
        apiInstance = cyperf.LicenseServersApi (self.apiClient)
        try:
            response = apiInstance.get_license_servers()
            servers  = [lData.host_name for lData in response.actual_instance if lData.connection_status == 'ESTABLISHED']
            if self.licenseServer in servers:
                pprint(f'License server {self.licenseServer} is already configured')
            else:
                lServer = cyperf.LicenseServerMetadata(host_name = self.licenseServer,
                                                       interactive_fingerprint_verification = False,
                                                       user = self.username,
                                                       password = self.password)
                #api_response = apiInstance.create_license_servers(license_server_metadata=[lServer])
                #pprint(api_instance)
        except cyperf.exceptions.ApiException as e:
            raise (e)

    def RefreshAgents(self):
        apiInstance = cyperf.AgentsApi(self.apiClient)
        try:
            response = apiInstance.get_agents() ## This is an object instead of a json
            ### [PARTHA] how do I access information from the following response
            agents   = response.actual_instance
            ### [PARTHA]
            for agent in agents:
                self.agents [agent.ip] = agent
        except cyperf.exceptions.ApiException as e:
            pprint (e)

    def LoadConfigs(self, configFiles):
        apiInstance = cyperf.ConfigurationsApi(self.apiClient)
        results     = []
        try:
            for cFile in configFiles:
                response = apiInstance.start_configs_import (cFile).await_completion()
                results += response

            #pprint(results)
            # Why isn't configUrl a part of AppsecConfig?
            configs = {}
            for elem in results:
                ### [PARTHA] Can we avoid translating json to an AppsecConfig object in the caller script?
                configs [elem['id']] = (elem['configUrl'], cyperf.AppsecConfig.from_dict(elem['configData']))
                ### [PARTHA]
        except cyperf.exceptions.ApiException as e:
            pprint (e)
        return configs

    def DeleteConfig(self, configs):
        apiInstance = cyperf.ConfigurationsApi(self.apiClient)
        for configUrl, config in configs.values():
            apiInstance.delete_configs (config.id)

    def LaunchSessions(self, configs):
        apiInstance = cyperf.SessionsApi(self.apiClient)
        sessions    = []
        for configUrl, config in configs.values():
            session = cyperf.Session()
            ## [PARTHA] Why cannot we use config.id in a consistent way?
            session.config_url = configUrl
            ## [PARTHA]
            sessions.append (session)
        try:
            ### [PARTHA] Ugly: Fix the following lines
            sessions = [apiInstance.get_sessions_by_id (session_id=session.id) for session in apiInstance.create_sessions(session=sessions)]
            for session in sessions:
                session.config = apiInstance.get_config(session_id=session.id).base_model
            ### [PARTHA]
            return sessions
        except cyperf.exceptions.ApiException as e:
            pprint (e)
            return []

    def CloseSessions(self, sessions):
        apiInstance = cyperf.SessionsApi(self.apiClient)
        for session in sessions:
            try:
                apiInstance.delete_sessions (session.id)
            except cyperf.exceptions.ApiException as e:
                pprint (f'{e}')

    def __updateObjective__(self, session, objective, duration):
        for tProfile in session.config.config.traffic_profiles:
            obj = tProfile.objectives_and_timeline.primary_objective
            if not duration:
                ### [PARTHA] Segment durations get reset as soon as the objective type is changed.
                ###          We need to find out a way to keep the existing segments even when the
                ###          objective type is changed.
                for segment in obj.timeline:
                    if segment.enabled:
                        ### [PARTHA] How can I avoid accessing base_model
                        segmentType = segment.segment_type.base_model
                        if segmentType == cyperf.SegmentType.STEADYSEGMENT or segmentType == cyperf.SegmentType.NORMALSEGMENT:
                            duration = segment.duration
                        ### [PARTHA]
                ### [PARTHA]
            obj.type = objective['type']
            obj.update()
            for segment in obj.timeline:
                if segment.enabled:
                    ### [PARTHA] How can I avoid accessing base_model
                    segmentType = segment.segment_type.base_model
                    ### [PARTHA]
                    if segmentType == cyperf.SegmentType.STEADYSEGMENT or segmentType == cyperf.SegmentType.NORMALSEGMENT:
                        segment.objective_value = objective['value']
                        segment.objective_unit  = objective['unit']
                        segment.duration        = duration
                        segment.update()

    def __updateAgents__(self, session, agentMapping):
        config      = session.config.config
        netProfiles = config.network_profiles
        for netProfile in netProfiles:
            ipNets = netProfile.ip_network_segment
            for ipNet in ipNets:
                if ipNet.name in agentMapping:
                    if not ipNet.agent_assignments:
                        ipNet.agent_assignments = cyperf.AgentAssignments()
                    agentDetails = [cyperf.AgentAssignmentDetails(agent_id = self.agents[agentName].id, id = self.agents[agentName].id) for agentName in agentMapping[ipNet.name]]
                    ipNet.agent_assignments.by_id.extend(agentDetails)
                    ipNet.agent_assignments.update()
                else:
                    pprint (f"Found no agents for the network segment {ipNet.name}")

    def UpdateSessionConfig(self, sessions, config):
        for session in sessions:
            self.__updateObjective__(session, config.objective, config.duration)
            self.__updateAgents__(session, config.agents)


    def StartSessions(self, sessions):
        apiInstance = cyperf.TestOperationsApi(self.apiClient)
        try:
            tests = [apiInstance.start_root_start_test(session_id = session.id) for session in sessions]
        except cyperf.exceptions.ApiException as e:
            pprint (e)

        for test in tests:
            try:
                result = test.await_completion()
                #pprint (result)
            ### [PARTHA] await_completion is generating generic Exception for API call failures.
            ###          It should generate cyperf.exceptions.ApiException or something else from
            ###          cyperf.exceptions
            #except cyperf.exceptions.ApiException as e:
            except Exception as e:
                pprint (e)
            ### [PARTHA]

    def WaitUntilStopped(self, sessions):
        apiInstance = cyperf.SessionsApi(self.apiClient)
        while sessions:
            time.sleep (0.5)
            tmpSessions = []
            for session in sessions:
                s = apiInstance.get_test (session_id = session.id)
                if s.status != 'STOPPED':
                    tmpSessions.append(session)
            sessions = tmpSessions

    def Run(self, config):
        width = 200
        pprint (f"Loading configuration {config.file} ...", width=width)
        configs  = self.LoadConfigs ([config.file])
        pprint (f"Launching session for configuration {config.file} ...", width=width)
        sessions = self.LaunchSessions (configs)
        pprint (f"Updating agents as {config.agents} ...", width=width)
        self.UpdateSessionConfig (sessions, config)
        pprint (f"Statrting session for configuration {config.file} ...", width=width)
        self.StartSessions(sessions)
        pprint (f"Started test for configuration {config.file} ... session id: {sessions[0].index}", width=width)
        self.WaitUntilStopped(sessions)
        pprint (f"Closing session for configuration {config.file} ...", width=width)
        self.CloseSessions (sessions)
        pprint (f"Deleting configuration {config.file} ...", width=width)
        self.DeleteConfig (configs)
        pprint (f"Deleted configuration {config.file} ...", width=width)

