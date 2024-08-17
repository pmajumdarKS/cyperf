from cyperf.utils.test import TestRunner, TestConfig

tests = [
    TestConfig ('samples/configs/Msoft_tput_smartNIC_passthru.zip', {'IP Network Segment 1': ['10.36.75.235'], 'IP Network Segment 2': ['10.36.75.246']}, 'Throughput', 12500000000, None)
]

runner = TestRunner ('10.36.75.241', 'admin', 'CyPerf&Keysight#1')

for config in tests:
    runner.Run (config)
