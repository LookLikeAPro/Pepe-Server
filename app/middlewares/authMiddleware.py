from django.utils.functional import SimpleLazyObject
from app.models import User

class AuthMiddleware(object):
	def process_request(self, request):
		assert hasattr(request, 'session'), ("AuthMiddleware unable to find session")
		if 'user' in request.session:
			user_email = request.session['user']
			request.user = SimpleLazyObject(lambda: User.objects.filter(email=user_email).first())
