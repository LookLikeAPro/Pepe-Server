from django.core.management.base import BaseCommand, CommandError
from subprocess import call, Popen, PIPE
import sys
import os
import signal
import atexit

class Command(BaseCommand):
	help = 'Runs "runserver" with webpack hot loader'

	# def add_arguments(self, parser):
	# 	parser.add_argument('poll_id', nargs='+', type=int)
	processes = []
	commands = [
		'python3 manage.py runserver',
		'npm run hot-dev-server',
	]

	def handle(self, *args, **options):
		atexit.register(self.killProcesses)
		self.startProcesses()
		while (1):
			inputBuffer = input('Press Q to Quit')
			if inputBuffer=='q' or inputBuffer=='Q':
				sys.exit()

	def startProcesses(self):
		self.processes = [Popen(cmd, stdout=PIPE, shell=True, preexec_fn=os.setsid) for cmd in self.commands]

	def killProcesses(self):
		[os.killpg(process.pid, signal.SIGTERM) for process in self.processes]
		print("Exited");
