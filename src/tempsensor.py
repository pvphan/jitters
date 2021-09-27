"""
DS18B20 1-wire temperature sensor
"""

# https://www.raspberrypi-spy.co.uk/2013/03/raspberry-pi-1-wire-digital-thermometer-sensor/
class TemperatureSensor:
    def __init__(self, pinNumber):
        pass

    def getTempC(self):
        raise NotImplementedError()
