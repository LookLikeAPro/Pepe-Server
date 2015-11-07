from django.conf.urls import include, url
from app import apis

urlpatterns = [
	url(r'', include('app.urls')),
]
