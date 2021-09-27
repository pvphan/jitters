import time
import threading

from gpiozero import PWMLED


class Relay:
    _offDutyValue = 0.0
    _sleepIncrement = 0.01
    _defaultCycleDuration = 30
    def __init__(self, pwmLed: PWMLED):
        self._led = pwmLed
        self._hardwareExecutionThread = threading.Thread()
        self._dutyValue = None
        self.setTargetDutyCycle(0.5)
        self._cycleDuration = None
        self.setCycleDuration(self._defaultCycleDuration)

    def setTargetDutyCycle(self, dutyValue):
        self._dutyValue = dutyValue

    def setCycleDuration(self, duration):
        self._cycleDuration = duration

    def startCycle(self):
        if self._hardwareExecutionThread.is_alive():
            return False
        self.canRunCycle = True
        self._hardwareExecutionThread = threading.Thread(
                target=self._setAndUnsetDutyValue,
                args=(self._cycleDuration,))
        self._hardwareExecutionThread.start()
        return True

    def killCycle(self):
        self.canRunCycle = False

    def isRunning(self):
        return self._hardwareExecutionThread.is_alive()

    def _setAndUnsetDutyValue(self, duration):
        self._led.value = self._dutyValue
        startTime = time.time()
        while time.time() - startTime < duration and self.canRunCycle:
            time.sleep(self._sleepIncrement)
        self._led.value = self._offDutyValue


def createRelayFromPin(pinNumber):
    pwmLed = PWMLED(pinNumber)
    return Relay(pwmLed)
