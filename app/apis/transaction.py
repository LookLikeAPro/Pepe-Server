from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render
from app.models import User
from app.models import Transaction

class byID(View):
	def get(self, request, *args, **kwargs):
		id = self.kwargs.get('id', None)
		if not id:
			return JsonResponse({'error':{'message':'Invalid Transaction ID'}})
		try:
			transaction = Transaction.objects.get(id=id)
		except:
			return JsonResponse({'error':{'message':'Transaction not found'}})
		transactionitems = transaction.transactionitem_set.all()
		transaction = transaction.to_dict()
		transaction['items'] = []
		[transaction['items'].append(item.to_dict(exclude=('transaction', 'id'))) for item in transactionitems]
		return JsonResponse(transaction)
