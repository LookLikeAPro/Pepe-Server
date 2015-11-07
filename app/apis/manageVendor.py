from django.http import JsonResponse
from django.views.generic import View
from app.models import User
from app.models import Transaction

import json

class create(View):
	def post(self, request, *args, **kwargs):
		if not hasattr(request, 'user'):
			return JsonResponse({'error':{'message':'Not logged in'}})
		try:
			data = json.loads(request.body.decode('utf-8'))
		except:
			return JsonResponse({'error':{'message':'Unable to parse request body'}})
		if (not 'name' in data) or (not 'email' in data):
			return JsonResponse({'error':{'message':'Invalid'}})
		# try:
		# 	user = User.objects.create(name="", email=email, password=password)
		# 	user.save()
		# except:
		# 	return JsonResponse({'error':{'message':'Signup Failed'}})
		return JsonResponse(data)
