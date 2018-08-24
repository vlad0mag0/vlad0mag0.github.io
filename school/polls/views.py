from django.shortcuts import render

from django.http import HttpResponse

def main(request):
	return render(request,"polls/index.html",
		{})

def index(request):
    return HttpResponse ("Hello, world. You're at the polls index.")
