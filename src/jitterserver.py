"""
The web application which will interact with users and control the underlying hardware
# https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
"""
import datetime

from flask import Flask, render_template

from relay import Relay
from tempsensor import TemperatureSensor


flaskApp = Flask("JitterServer")

class JitterServer:
    _indexHtmlPath = "index.html"
    def __init__(self,
                heaterSensor: TemperatureSensor,
                heaterRelay: Relay,
                pump1Relay: Relay,
                pump2Relay: Relay):
        self._heaterSensor = heaterSensor
        self._heaterRelay = heaterRelay
        self._pump1Relay = pump1Relay
        self._pump2Relay = pump2Relay

    def index(self):
        now = datetime.datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M:%S")
        templateData = {
                "title": "Jitter Server",
                "time": timeString,
                "isPump1On": self._pump1Relay.isRunning(),
        }
        return render_template(self._indexHtmlPath, **templateData)


class GlobalContainer:
    jitterServer = None


@flaskApp.route("/")
def index():
    return GlobalContainer.jitterServer.index()


@flaskApp.route("/pump1/startcycle", methods=["GET", "POST"])
def pump1StartCycle():
    didStart = GlobalContainer.jitterServer._pump1Relay.startCycle()
    return index()


@flaskApp.route("/pump1/killcycle", methods=["GET", "POST"])
def pump1KillCycle():
    didKill = GlobalContainer.jitterServer._pump1Relay.killCycle()
    return index()


def runJitterServer(heaterSensor, heaterRelay, pump1Relay, pump2Relay,
        port, shouldDebug):
    GlobalContainer.jitterServer = JitterServer(heaterSensor, heaterRelay,
            pump1Relay, pump2Relay)
    localhost = "0.0.0.0"
    flaskApp.run(debug=shouldDebug, port=port, host=localhost)
