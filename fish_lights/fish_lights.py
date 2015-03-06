#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import json
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv

def check_switch():
	t = open('json/light.json', 'r')
	data = json.loads(t.read(), object_hook=_decode_dict)
	t.close()
	return data

def toggle():
	GPIO.output(23, 1)
	time.sleep(0.5)
	GPIO.output(23, 0)

def off():
	data = check_switch()
	if data["light"] == 1:
		toggle()
		data["light"] = 0
		update(data)
def on():
	data = check_switch()
	if data["light"] == 0:
		toggle()
		data["light"] = 1
		update(data)
def update(data):
	f = open("json/light.json", 'w')
	f.write(json.dumps(data, ensure_ascii=True))
	f.close()
try:
	while True:
		#time.sleep(1)
		data = check_switch()
		if data["switch"] == 0:
			off()
		elif data["switch"] == 1:
			on()
finally:
	GPIO.cleanup()
