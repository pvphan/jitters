from unittest.mock import MagicMock

from jitterserver import runJitterServer


def main():
    heaterSensor = MagicMock()
    heaterSensor.getTempC.return_value = 11.1
    heaterRelay = MagicMock()
    pump1Relay = MagicMock()
    pump2Relay = MagicMock()

    port = 8080
    shouldDebug = True
    runJitterServer(heaterSensor, heaterRelay, pump1Relay, pump2Relay,
            port, shouldDebug)


if __name__ == "__main__":
    main()
