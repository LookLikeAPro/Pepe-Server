from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render
from app.models import User

class login(View):
	def get(self, request, *args, **kwargs):
		if (not 'email' in request.GET) or (not 'password' in request.GET):
			return JsonResponse({'error':{'message':'Invalid parameters'}})
		email = request.GET['email']
		password = request.GET['password']
		user = User.objects.filter(email=email).first()
		if (not user) or (user.password != password):
			return JsonResponse({'error':{'message':'Invalid username or password'}})
		request.session['user'] = user.email
		return JsonResponse({
			"email": user.email,
			"name": user.name
		})

class logout(View):
	def get(self, request, *args, **kwargs):
		try:
			del request.session['user']
		except KeyError:
			return JsonResponse({'status':'success'})
		return JsonResponse({'status':'success'})

class signup(View):
	def get(self, request, *args, **kwargs):
		if (not 'email' in request.GET) or (not 'password' in request.GET):
			return JsonResponse({'error':{'message':'Invalid parameters'}})
		email = request.GET['email']
		password = request.GET['password']
		try:
			user = User.objects.create(name="", email=email, password=password)
			user.save()
		except:
			return JsonResponse({'error':{'message':'Signup Failed'}})
		request.session['user'] = user.email
		return JsonResponse({
			"status": "success"
		})
