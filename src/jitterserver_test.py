from unittest.mock import MagicMock

from jitterserver import runJitterServer
from relay import Relay


def main():
    heaterSensor = MagicMock()
    heaterSensor.getTempC.return_value = 11.1

    heaterLed = MagicMock()
    heaterRelay = Relay(heaterLed)

    pwmLed1 = MagicMock()
    pump1Relay = Relay(pwmLed1)
    pump1Relay.setCycleDuration(5)

    pwmLed2 = MagicMock()
    pump2Relay = Relay(pwmLed2)
    pump2Relay.setCycleDuration(5)

    port = 8080
    shouldDebug = True
    runJitterServer(heaterSensor, heaterRelay, pump1Relay, pump2Relay,
            port, shouldDebug)


if __name__ == "__main__":
    main()
