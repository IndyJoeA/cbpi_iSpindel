import os
from subprocess import Popen, PIPE, call

from modules import cbpi
from modules.core.hardware import ActorBase, SensorPassive, SensorActive
import json
from flask import Blueprint, render_template, jsonify, request
from modules.core.props import Property

blueprint = Blueprint('hydrometer', __name__)
cache = {}

@cbpi.sensor
class Hydrometer(SensorActive):
	key = Property.Text(label="Sensor ID", configurable=True)
	sensorType = Property.Select("Data Type", options=["Temperature", "Angle", "Battery"])

	def execute(self):
		global cache
		while self.is_running():
			try:
				value = cache.pop(self.key, None)
				if value is not None:
					self.data_received(value)
			except:
				pass
			self.api.socketio.sleep(1) 

@blueprint.route('/api/hydrometer/v1/data', methods=['POST'])
def set_temp():
	global cache
	
	data = request.get_json()
	id = data["name"]
	temp = data["temperature"]
	angle = data["angle"]
	battery = data["battery"]
		
	cache[id] = temp
	return ('', 204)

@cbpi.initalizer()
def init(cbpi):
	print "INITIALIZE HYDROMETER MODULE"
	cbpi.app.register_blueprint(blueprint)
	print "READY"
