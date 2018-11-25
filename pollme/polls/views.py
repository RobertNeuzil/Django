from django.shortcuts import render
from django.http import HttpResponse
from . models import Poll


def polls_list(request):
	'''
	renders polls_list template along with the currently available polls, in context

	'''

	polls = Poll.objects.all()
	context = {
	
	"polls": polls
	
	}
	return render(request, "polls/polls_list.html", context)
# Create your views here.
