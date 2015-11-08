import math
import os
import uuid
from django.core.management.base import BaseCommand, CommandError
from app.models import Picture

pepe_dir = './static/pepes/'

def register_pic(filename):
	print('register '+filename)
	random = str(uuid.uuid4())[:8]
	filename_new = random+'.'+filename.split('.')[-1]
	os.rename(pepe_dir+filename, pepe_dir+filename_new)
	Picture.objects.create(asset=filename_new).save()

class Command(BaseCommand):
	help = 'organizes and catalogs pepes'

	def handle(self, *args, **options):
		for root, dirs, filenames in os.walk(pepe_dir):
			for filename in filenames:
				if filename.endswith('png') or filename.endswith('gif') or filename.endswith('jpg'):
					try:
						Picture.objects.get(asset=filename)
					except:
						register_pic(filename)
		for picture in Picture.objects.all():
			if not os.path.isfile(pepe_dir+picture.asset):
				print('remove '+picture.asset)
				picture.delete()
		self.stdout.write('Complete')
