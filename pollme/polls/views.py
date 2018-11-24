from django.shortcuts import render
from django.http import HttpResponse



def polls_list(request):
	return HttpResponse('This is the polls list')
# Create your views here.
