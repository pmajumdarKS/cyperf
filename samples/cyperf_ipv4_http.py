from cyperf import ObjectiveType
from cyperf.utils.test import TestRunner, TestConfig

tests = [
    TestConfig ('samples/configs/Msoft_tput_smartNIC_passthru.zip', {'IP Network Segment 1': ['10.36.74.185'], 'IP Network Segment 2': ['10.36.74.196']}, ObjectiveType.THROUGHPUT, '15 Gbps'),
    TestConfig ('samples/configs/Msoft_tput_smartNIC_passthru.zip', {'IP Network Segment 1': ['10.36.74.185'], 'IP Network Segment 2': ['10.36.74.196']})
]

runner = TestRunner ('10.36.75.169', 'admin', 'CyPerf&Keysight#1', licenseServer = '10.38.167.200')

for config in tests:
    runner.Run (config)
