from django.http import JsonResponse
from django.views.generic import View
from django.template import RequestContext, loader
from django.shortcuts import render
from app.models import Vendor

class bySlug(View):
	def get(self, request, *args, **kwargs):
		slug = self.kwargs.get('slug', None)
		if not slug:
			return JsonResponse({'error':{'message':'Invalid Link'}})
		try:
			vendor = Vendor.objects.get(slug=slug)
		except:
			return JsonResponse({'error':{'message':'Invalid Link'}})
		return JsonResponse(vendor.to_dict())

class nearby(View):
	def get(self, request, *args, **kwargs):
		vendors = Vendor.objects.filter().all()
		vendors_dict = []
		for vendor in vendors:
			vendors_dict.append(vendor.to_dict())
		return JsonResponse({
			"data": vendors_dict
		})

class discover(View):
	def get(self, request, *args, **kwargs):
		vendors = Vendor.objects.filter().all()[5:10]
		vendors_dict = []
		for vendor in vendors:
			vendors_dict.append(vendor.to_dict())
		return JsonResponse({
			"data": vendors_dict
		})
