#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import os
import subprocess
import sublime

class CommandsPy(object):
	def __init__(self):
		super(CommandsPy, self).__init__()
		self.error_running = False

	def runCommand(self, command, cwd=None,setReturn=False,verbose=False):
		process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,cwd=cwd, universal_newlines=True,shell=True)#
		output = process.communicate()

		stdout = output[0]
		stderr = output[1]

		return_code = process.returncode

		if(verbose):
			print(stdout)
			print(stderr)

		if(return_code != 0):			
			self.error_running = True

		if(setReturn):
			return stdout