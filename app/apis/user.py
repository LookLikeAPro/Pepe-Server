from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render
from app.models import User

class current(View):
	def get(self, request, *args, **kwargs):
		if not hasattr(request, 'user'):
			return JsonResponse({'error':{'message':'Not logged in'}})
		user = request.user
		return JsonResponse(user.to_dict())

class byID(View):
	def get(self, request, *args, **kwargs):
		id = self.kwargs.get('id', None)
		if not id:
			return JsonResponse({'error':{'message':'Invalid User ID'}})
		user = User.objects.filter(id=id).first()
		if not user:
			return JsonResponse({'error':{'message':'User not found'}})
		return JsonResponse(user.to_dict())
