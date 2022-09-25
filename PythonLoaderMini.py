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
		name = os.path.splitext(os.path.split(plugin_path)[1])[0]
	elif opt_name == "--connect":
		opt_value = str(opt_value).split(":")
		host, port = opt_value
		port = int(port)

print(host, port, path, name)  # type: ignore
Plugin(host, port, path, name)  # type: ignore
