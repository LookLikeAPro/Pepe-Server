from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .apis import *
from .views import *

def generate_patterns(prefix, urls):
	patterns = []
	for key, subset in urls.items():
		if isinstance(subset, dict):
			if prefix != '':
				patterns = generate_patterns(prefix+'/'+key, subset) + patterns
			else:
				patterns = generate_patterns(key, subset) + patterns
		else:
			patterns.append(url(r'^'+prefix+'/'+key, subset.as_view()))
	return patterns

urls = {
	'api': {
		'auth': {
			'facebook/signup': error.noApi,
			'twitter/signup': error.noApi,
			'login': auth.login,
			'logout': auth.logout,
			'signup': auth.signup
		},
		'user': {
			'current': user.current,
			'(?P<id>\w{0,20})/edit': error.noApi,
			'by-id/(?P<id>\w{0,20})': user.byID
		},
		'transaction': {
			'by-id/(?P<id>\w{0,20})': transaction.byID
		},
		'vendor': {
			'nearby': vendor.nearby,
			'discover': vendor.discover,
			'by-slug/(?P<slug>\w{0,50})': vendor.bySlug,
			'featured': error.noApi
		},
		'manage': {
			'vendor': {
				'create': manageVendor.create,
				'(?P<slug>\w{0,50})/edit': error.noApi,
				'(?P<slug>\w{0,50})': {
					'collaborator': {
						'': error.noApi,
						'add': error.noApi,
						'edit': error.noApi,
						'remove': error.noApi
					}
				}
			}
		},
		'': error.noApi
	},
	'?': app
}

urlpatterns = generate_patterns('', urls)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
