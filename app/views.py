from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext, loader
import json
from subprocess import call

class app(View):
	def get(self, request, *args, **kwargs):
		template = loader.get_template('app.html')
		with open('static/client/stats.json') as stats_file:    
			stats = json.load(stats_file)
		public_path = stats['publicPath']
		cache_hash = stats['hash']
		if public_path.find('localhost') > -1:
			livereload = True
		else:
			livereload = False
		prerender = False
		# switch to analysing stats.json later, there may be multiple files
		if livereload:
			stylesheets = []
		else:
			stylesheets = [public_path+'main.css'+'?'+cache_hash]
		scripts = [public_path+'main.js'+'?'+cache_hash]
		if prerender:
			process = call(["ls", "-l"])
			prerender_content = process.communicate()
		else:
			prerender_content = ""
			# $content = exec("node ../client-config/server-executed.js --path=$path");
		context = RequestContext(request, {
			"stylesheets": stylesheets,
			"prerender": prerender_content,
			"preload_data": "{}",
			"scripts": scripts,
		})
		return HttpResponse(template.render(context))
