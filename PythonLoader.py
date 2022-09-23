#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys, getopt, os
from PythonLoaderCore import Plugin

plugin_path = host = port = None

opts = getopt.getopt(sys.argv[1:], "", longopts=["load=", "connect="])[0]
print(opts)
for opt_name, opt_value in opts:
	if opt_name == "--load":
		path = plugin_path = str(opt_value)
		if os.access(plugin_path, os.W_OK) == False:
			print("Error: Wrong path!")
			sys.exit(-1)
		name = os.path.splitext(os.path.split(plugin_path)[1])[0]
	elif opt_name == "--connect":
		opt_value = str(opt_value).split(":")
		if len(opt_value) == 2:
			host, port = opt_value
			port = int(port)
		else:
			print("Error: Wrong port!")
			sys.exit(-1)
	else:
		print(f"Error: Wrong param:{opt_name}={opt_value}!")
		sys.exit(-1)
if (plugin_path or host or port) == False:
	print("Error: More param!")
	sys.exit(-1)

print(host, port, path, name)  # type: ignore
Plugin(host, port, path, name)  # type: ignore
