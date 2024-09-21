from cyperf import ObjectiveType, TestRunner, TestConfig

tests = [
    TestConfig ('samples/configs/Msoft_tput_smartNIC_passthru.zip', {'IP Network Segment 1': ['10.36.74.185'], 'IP Network Segment 2': ['10.36.74.196']}, ObjectiveType.THROUGHPUT, '15 Gbps'),
    TestConfig ('samples/configs/Msoft_tput_smartNIC_passthru.zip', {'IP Network Segment 1': ['10.36.74.185'], 'IP Network Segment 2': ['10.36.74.196']})
]

runner = TestRunner ('10.36.75.169', 'admin', 'CyPerf&Keysight#1', licenseServer = 'slum-3-0.buh.is.keysight.com')
#runner = TestRunner ('10.36.75.169', 'admin', 'CyPerf&Keysight#1', licenseServer = '10.38.167.200')
#runner = TestRunner ('10.36.75.169', 'admin', 'CyPerf&Keysight#1', licenseServer = '3.135.19.236')

for config in tests:
    runner.Run (config)
