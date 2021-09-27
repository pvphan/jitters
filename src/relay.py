from gpiozero import PWMLED

class Relay:
    def __init__(self, pinNumber):
        self._dutyValue = 0
        self._led = PWMLED(pinNumber)
        self.setDutyCycle(0)

    def setDutyCycle(self, dutyValue):
        self._led.value = dutyValue
