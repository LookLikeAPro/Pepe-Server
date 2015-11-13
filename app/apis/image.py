from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render
from app.models import Picture

class random(View):
	def get(self, request, *args, **kwargs):
		if not 'quantity' in request.GET:
			quantity = 1
		else:
			quantity = int(request.GET['quantity'])
		if quantity == 1:
			picture = Picture.objects.random().to_dict(exclude=('dhash'))
			picture['asset'] = '/static/pepes/' + picture['asset']
			return JsonResponse({
				"images": [picture]
			})
		else:
			pictures = []
			for i in range(0, quantity):
				picture = Picture.objects.random().to_dict(exclude=('dhash'))
				picture['asset'] = '/static/pepes/' + picture['asset']
				pictures.append(picture)

			return JsonResponse({
				"images": pictures
			})

class slug(View):
	def get(self, request, *args, **kwargs):
		slug = self.kwargs.get('slug', None)
		if not slug:
			return JsonResponse({'error':{'message':'Invalid Slug'}})
		try:
			picture = Picture.objects.get(uuid=slug)
		except:
			return JsonResponse({'error':{'message':'Image unavaliable'}})
		return JsonResponse(picture.to_dict())
