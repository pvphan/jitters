"""
Main application launch: connect to hardware components, inject them into the
    web server, begin serving web requests.
"""

from jitterserver import runJitterServer
from relay import Relay
from tempsensor import TemperatureSensor


def main():
    # TODO: map pinout to physical layout (not set up yet)
    heaterSensor = TemperatureSensor(None)
    heaterRelay = Relay(None)
    pump1Relay = Relay(None)
    pump2Relay = Relay(None)

    port = 80
    shouldDebug = False
    runJitterServer(heaterSensor, heaterRelay, pump1Relay, pump2Relay,
            port, shouldDebug)


if __name__ == "__main__":
    main()
