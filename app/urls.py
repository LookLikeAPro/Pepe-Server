from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .apis import *
from .views import *

def generate_patterns(prefix, urls):
	patterns = []
	for key, subset in urls.items():
		if isinstance(subset, dict):
			if prefix == '':
				patterns = generate_patterns(key, subset) + patterns
			else:
				patterns = generate_patterns(prefix+'/'+key, subset) + patterns
		else:
			if prefix == '':
				patterns.append(url(r'^'+key+'/?', subset.as_view()))
			else:
				patterns.append(url(r'^'+prefix+'/'+key+'/?', subset.as_view()))
	return patterns

urls = {
	'api': {
		'image': {
			'random': image.random,
			'slug': {
				'(?P<slug>\w{0,8})': image.slug
			}
		},
		'': error.noApi
	},
	'image/(?P<slug>\w{0,8})': slug,
	'random': random,
}

urlpatterns = generate_patterns('', urls)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
