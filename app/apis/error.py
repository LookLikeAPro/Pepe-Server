from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render

class noApi(View):
	def get(self, request, *args, **kwargs):
		return JsonResponse({'error':{'message':'No such API endpoint'}})
	def post(self, request, *args, **kwargs):
		return JsonResponse({'error':{'message':'No such API endpoint'}})
