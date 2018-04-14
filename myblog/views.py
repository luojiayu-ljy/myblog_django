from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from myblog.models import BlogsPost

# Create your views here.
def archive(request):
	posts = BlogsPost.objects.all()
	t = loader.get_template('archive.html')
	c = {'posts':posts}
	return HttpResponse(t.render(c))