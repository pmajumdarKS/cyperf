import sys
import time
import datetime
import re
import urllib3
from pprint import pprint

import cyperf

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

    def __init__(self, controller, username="", password="", refreshToken="", licenseServer = None):
        self.host          = f'https://{controller}'
        self.username      = username
        self.password      = password
        self.refreshToken  = refreshToken
        self.licenseServer = licenseServer

        self.configuration = cyperf.Configuration(host = self.host)
        self.configuration.verify_ssl = False
        self.apiClient     = cyperf.ApiClient(self.configuration)
        self.addedLicenseServers      = []
        self.agents        = {}

        self.configuration.access_token = self.__authorize__()

        self.UpdateLicenseServer()
        self.RefreshAgents()

    def __del__(self, time=time, datetime=datetime):
        if not sys.modules ['time']:
            sys.modules ['time'] = time
        self.RemoveLicenseServer()

    def __authorize__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        apiInstance = cyperf.AuthorizationApi(self.apiClient)
        grantType   = "refresh_token" if self.refreshToken else "password"
        try:
            response = apiInstance.auth_realms_keysight_protocol_openid_connect_token_post (client_id     = TestRunner.WAP_CLIENT_ID,
                                                                                            grant_type    = grantType,
                                                                                            password      = self.password,
                                                                                            username      = self.username,
                                                                                            refresh_token = self.refreshToken)
            return response.access_token
        except cyperf.ApiException as e:
            raise (e)

    def Authorize(self):
        self.configuration.access_token = self.__authorize__()

    def UpdateLicenseServer (self):
        if not self.licenseServer:
            return
        apiInstance = cyperf.LicenseServersApi (self.apiClient)
        try:
            response = apiInstance.get_license_servers()
            servers  = [lData.host_name for lData in response]
            if self.licenseServer in servers:
                pprint(f'License server {self.licenseServer} is already configured')
            else:
                lServer = cyperf.LicenseServerMetadata(host_name = self.licenseServer,
                                                       trust_new = True,
                                                       user = self.username,
                                                       password = self.password)
                newServers = apiInstance.create_license_servers(license_server_metadata=[lServer])
                while newServers:
                    for server in newServers:
                        ### [PARTHA] If get_license_servers_by_id expects a string as id then
                        ###          LicenseServerMetadata shoud have it as a string. User shouldn't
                        ###          need to change the type.
                        s = apiInstance.get_license_servers_by_id(str(server.id))
                        ### [PARTHA]
                        if 'IN_PROGRESS' != s.connection_status:
                            newServers.remove(server)
                            self.addedLicenseServers.append(server)
                            if 'ESTABLISHED' == s.connection_status:
                                print (f'Successfully added license server {s.host_name}')
                            else:
                                print (f'Could not connect to license server {s.host_name}')
                    time.sleep(0.5)
        except cyperf.ApiException as e:
            raise (e)

    def RemoveLicenseServer (self):
        apiInstance = cyperf.LicenseServersApi (self.apiClient)
        for server in self.addedLicenseServers:
            try:
                apiInstance.delete_license_servers(str(server.id))
            except cyperf.ApiException as e:
                pprint (f'{e}')

    def RefreshAgents(self):
        apiInstance = cyperf.AgentsApi(self.apiClient)
        try:
            agents = apiInstance.get_agents() ## This is an object instead of a json
            for agent in agents:
                self.agents [agent.ip] = agent
        except cyperf.ApiException as e:
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
                configs [elem['id']] = (elem['configUrl'], cyperf.AppsecConfig.from_dict(elem))
                ### [PARTHA]
        except cyperf.ApiException as e:
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
            sessions = apiInstance.create_sessions(sessions)
            return sessions
        except cyperf.ApiException as e:
            pprint (e)
            return []

    def CloseSessions(self, sessions):
        apiInstance = cyperf.SessionsApi(self.apiClient)
        for session in sessions:
            try:
                apiInstance.delete_sessions (session.id)
            except cyperf.ApiException as e:
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
                        segmentType = segment.segment_type
                        if segmentType == cyperf.SegmentType.STEADYSEGMENT or segmentType == cyperf.SegmentType.NORMALSEGMENT:
                            duration = segment.duration
                ### [PARTHA]
            obj.type = objective['type']
            obj.update()
            for segment in obj.timeline:
                if segment.enabled:
                    segmentType = segment.segment_type
                    if segmentType == cyperf.SegmentType.STEADYSEGMENT or segmentType == cyperf.SegmentType.NORMALSEGMENT:
                        segment.objective_value = objective['value']
                        segment.objective_unit  = objective['unit']
                        segment.duration        = duration
            obj.update()

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
            tests = [apiInstance.start_test_start(session_id = session.id) for session in sessions]
        except cyperf.ApiException as e:
            pprint (e)

        for test in tests:
            try:
                result = test.await_completion()
                #pprint (result)
            except cyperf.ApiException as e:
                pprint (e)

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

    def __CollectStats__(self, session):
        apiInstance = cyperf.StatisticsApi(self.apiClient)
        try:
            resp = apiInstance.get_stats(session.test.test_id)
            stats = {}
            for stats_group in resp:
                stat  = apiInstance.get_stats_by_id(session.test.test_id, stats_group.name)
                stats [stat.name] = stat
            return stats
        except cyperf.exceptions.ApiException as e:
            pprint (f'{e}')

    def CollectStats(self, sessions):
        return [self.__CollectStats__(session) for session in sessions]

    def __Analyze__(self, stats):
        statDict = {}
        for statName in stats:
            pprint(statName)
            stat = stats[statName]
            statDict[statName] = {}
            if stat.snapshots:
                for snapshot in stat.snapshots:
                    timeStamp = snapshot.timestamp
                    statDict[statName][timeStamp] = []
                    for val in snapshot.values:
                        d = dict(zip(stat.columns, [data.actual_instance for data in val]))
                        statDict[statName][timeStamp].append(d)

        pprint (statDict)
        return True

    def Analyze(self, stats):
        return [self.__Analyze__(s) for s in stats]

    def Run(self, config):
        width = 200
        pprint (f"Loading configuration {config.file} ...", width=width)
        configs  = self.LoadConfigs ([config.file])
        pprint (f"Launching session for configuration {config.file} ...", width=width)
        sessions = self.LaunchSessions (configs)
        pprint (f"Updating agents as {config.agents} ...", width=width)
        self.UpdateSessionConfig (sessions, config)
        pprint (f"Starting session for configuration {config.file} ...", width=width)
        self.StartSessions(sessions)
        pprint (f"Started test for configuration {config.file} ... session id: {sessions[0].index}", width=width)
        self.WaitUntilStopped(sessions)
        pprint (f"Collecting stats for configuration {config.file} ...", width=width)
        stats = self.CollectStats(sessions)
        if False in self.Analyze(stats):
            pprint (f"Test Failed for {config.file}")
        else:
            pprint (f"Test Passed for {config.file}")
        pprint (f"Closing session for configuration {config.file} ...", width=width)
        self.CloseSessions (sessions)
        pprint (f"Deleting configuration {config.file} ...", width=width)
        self.DeleteConfig (configs)
        pprint (f"Deleted configuration {config.file} ...", width=width)

