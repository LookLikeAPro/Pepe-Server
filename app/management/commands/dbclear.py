from django.core.management.base import BaseCommand, CommandError
import app.models as models

class Command(BaseCommand):
	help = 'Clears app models'

	# def add_arguments(self, parser):
	# 	parser.add_argument('poll_id', nargs='+', type=int)

	def handle(self, *args, **options):
		models.User.objects.all().delete()
		models.Vendor.objects.all().delete()
		models.VendorManagement.objects.all().delete()
		models.Product.objects.all().delete()
		models.Transaction.objects.all().delete()
		models.TransactionItem.objects.all().delete()
		models.CartItem.objects.all().delete()
		self.stdout.write('Successfully Deleted')
