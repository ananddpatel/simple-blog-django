from django.shortcuts import render
from django.views import generic 
from . import models as my_models

# Create your views here.

class BlogIndex(generic.ListView):
	queryset = my_models.Entry.objects.published()
	template_name = "index.html"
	paginate_by = 3 # number of entries to show per page

class BlogDetail(generic.DetailView):
	model = my_models.Entry
	template_name = 'post.html'