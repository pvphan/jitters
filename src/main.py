"""
Main application launch: connect to hardware components, inject them into the
    web server, begin serving web requests.
"""

from jitterserver import JitterServer
from relay import Relay
from tempsensor import TemperatureSensor


def main():
    heaterSensor = TemperatureSensor(None)
    heaterRelay = Relay(None)
    pump1Relay = Relay(None)
    pump2Relay = Relay(None)

    jitterServer = JitterServer(heaterSensor, heaterRelay, pump1Relay, pump2Relay)
    jitterServer.run()


if __name__ == "__main__":
    main()
