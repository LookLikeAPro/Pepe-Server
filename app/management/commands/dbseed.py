import math
from django.core.management.base import BaseCommand, CommandError
import app.models as models

class Command(BaseCommand):
	help = 'Clears app models'

	# def add_arguments(self, parser):
	# 	parser.add_argument('poll_id', nargs='+', type=int)

	def handle(self, *args, **options):
		self.seedUser()
		self.seedVendor()
		self.seedVendorManagement()
		self.seedProduct()
		self.seedTransaction()
		self.stdout.write('Seeding complete')

	def seedUser(self):
		models.User.objects.create(name='Jerry Zhou', email='test@test.com', password='123456').save()
		for i in range(0, 200):
			email = str(i)+'@test.com'
			models.User.objects.create(name=i, email=email, password=i).save()

	def seedVendor(self):
		for i in range(0, 20):
			name = 'shop'+str(i)
			email = 'shop'+str(i)+'@solanum.com'
			slug = 'shop'+str(i)
			description = 'test'
			phone_number = '111111'+str(i)
			models.Vendor.objects.create(name=name, email=email, slug=slug, description=description, phone_number=phone_number).save()

	def seedVendorManagement(self):
		#Do not use "Through" type ManyToMany if it is only two columns. This is more work.
		#This exists because there are intricacies in relationship between venor and user (permission level etc)
		for i in range(0, 20):
			user = models.User.objects.get(name=str(i))
			vendor = models.Vendor.objects.get(name='shop'+str(i))
			models.VendorManagement.objects.create(user=user, vendor=vendor).save()

	def seedProduct(self):
		for i in range(0, 200):
			name = 'product'+str(i)
			price = i
			description = 'WTF'
			vendor = models.Vendor.objects.get(name='shop'+str(int(math.floor(i/20))))
			models.Product.objects.create(name=name, description=description, price=price, vendor=vendor).save()

	def seedTransaction(self):
		for i in range(0, 400):
			amount = i
			vendor = models.Vendor.objects.get(name='shop'+str(int(math.floor(i/20))))
			user = models.User.objects.get(name=str(int(math.floor(i/2))))
			transaction = models.Transaction.objects.create(amount=amount, user=user, vendor=vendor)
			transaction.save()
			for i in range(0, 3):
				product = models.Product.objects.get(name='product1')
				models.TransactionItem.objects.create(transaction=transaction, product=product, amount=1, count=1).save()

