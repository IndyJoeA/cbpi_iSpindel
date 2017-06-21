# -*- coding: utf-8 -*-
import os
from subprocess import Popen, PIPE, call

from modules import cbpi, socketio
from modules.core.hardware import SensorActive
import json
from flask import Blueprint, render_template, jsonify, request
from modules.core.props import Property

blueprint = Blueprint('hydrometer', __name__)
cache = {}

def calcGravity(polynom, tilt):
	# Calculate gravity from polynomial
	tilt = float(tilt)
	result = eval(polynom)
	result = round(float(result),2)
	return result

@cbpi.sensor
class Hydrometer(SensorActive):
	key = Property.Text(label="Sensor ID", configurable=True)
	sensorType = Property.Select("Data Type", options=["Temperature", "Gravity", "Battery"])
	tuningPolynom = Property.Text(label="Tuning Polynomial", configurable=True, default_value="tilt")
	unitsGravity = Property.Select("Gravity Units", options=["SG", "Brix", "°P"])

	def get_unit(self):
		if self.sensorType == "Temperature":
			return "°C" if self.get_config_parameter("unit", "C") == "C" else "°F"
		elif self.sensorType == "Gravity":
			return self.unitsGravity
		elif self.sensorType == "Battery":
			return "%"
		else:
			return " "

	def stop(self):
		pass

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

	for idx, value in cbpi.cache["sensors"].iteritems():
		if type(value.instance) is Hydrometer:
			if value.instance.sensorType == "Temperature":
				cache[id] = temp
			elif value.instance.sensorType == "Gravity":
				cache[id] = calcGravity(value.instance.tuningPolynom, angle)
			elif value.instance.sensorType == "Battery":
				cache[id] = battery

	return ('', 204)

@cbpi.initalizer()
def init(cbpi):
	print "INITIALIZE HYDROMETER MODULE"
	cbpi.app.register_blueprint(blueprint)
	print "READY"
