import os
import uuid
from django.core.management.base import BaseCommand, CommandError
from app.models import Picture
from app.helpers.dhash import dhash
from PIL import Image 

pepe_dir = './static/pepes/'

def register_pic(filename):
	hash_val = dhash(Image.open(pepe_dir+filename), hash_size = 128)
	if Picture.objects.filter(dhash=hash_val).count() > 0:
		print('duplicate: '+ filename + ' ' + Picture.objects.filter(dhash=hash_val).first().asset)
		return
	random = str(uuid.uuid4())[:8]
	filename_new = random+'.'+filename.split('.')[-1]
	Picture.objects.create(uuid=random, asset=filename, dhash=hash_val).save()
	print('registered: ' + filename)

class Command(BaseCommand):
	help = 'Organizes and catalogs pepes'
	def handle(self, *args, **options):
		for root, dirs, filenames in os.walk(pepe_dir):
			for filename in filenames:
				if filename.endswith('png') or filename.endswith('gif') or filename.endswith('jpg'):
					if Picture.objects.filter(asset=filename).count() > 0:
						pass
					else:
						register_pic(filename)
		for picture in Picture.objects.all():
			if not os.path.isfile(pepe_dir+picture.asset):
				print('remove '+picture.asset)
				picture.delete()
		self.stdout.write('Complete')
