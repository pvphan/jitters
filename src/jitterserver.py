"""
The web application which will interact with users and control the underlying hardware
"""

from relay import Relay
from tempsensor import TemperatureSensor

# https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
class JitterServer:
    def __init__(self,
            heaterSensor: TemperatureSensor,
            heaterRelay: Relay,
            pump1Relay: Relay,
            pump2Relay: Relay):
        self._heaterSensor = heaterSensor
        self._heaterRelay = heaterRelay
        self._pump1Relay = pump1Relay
        self._pump2Relay = pump2Relay

    def run(self):
        raise NotImplementedError()
