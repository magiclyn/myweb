from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.1111111")

def detail(request,question_id):
	return HttpResponse("Your'are looking at question %s." % question_id)


def results(request,question_id):
	return HttpResponse("You're looking at the Results of question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)