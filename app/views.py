from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext, loader
from app.models import Picture

class random(View):
	def get(self, request, *args, **kwargs):
		template = loader.get_template('app.html')
		picture = Picture.objects.random().to_dict()
		picture['asset'] = '/static/pepes/' + picture['asset']
		context = RequestContext(request, {
			"picture": picture
		})
		return HttpResponse(template.render(context))

class slug(View):
	def get(self, request, *args, **kwargs):
		slug = self.kwargs.get('slug', None)
		if not slug:
			return JsonResponse({'error':{'message':'Invalid Slug'}})
		try:
			picture = Picture.objects.get(uuid=slug)
		except:
			return JsonResponse({'error':{'message':'Image unavaliable'}})
		template = loader.get_template('app.html')
		picture = picture.to_dict()
		picture['asset'] = '/static/pepes/' + picture['asset']
		context = RequestContext(request, {
			"picture": picture
		})
		return HttpResponse(template.render(context))
