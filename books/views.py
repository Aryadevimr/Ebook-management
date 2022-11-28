from django.shortcuts import render
from django.http import HttpResponse
from .models import Books
# Create your views here.
def index(request):
	books = Books.objects.all()
	return render(request,'index.html',{'books':books})
	#return HttpResponse("<h1> Welcome to Ebook</h1>")
def about(request):
	return HttpResponse("<h1> About page</h1>")
def review(request):
	return HttpResponse("<h1> Review</h1>")
