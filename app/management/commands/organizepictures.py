import math
import os
from django.core.management.base import BaseCommand, CommandError
from app.models import Picture

dir = '/static/pepes'

class Command(BaseCommand):
	help = 'organizes and catalogs pepes'

	def handle(self, *args, **options):
		for root, dirs, filenames in os.walk(indir):
			for f in filenames:
				print(f)
		self.stdout.write('Seeding complete')


