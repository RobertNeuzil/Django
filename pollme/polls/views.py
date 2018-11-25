from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Poll, Choice


def polls_list(request):
	'''
	renders polls_list template along with the currently available polls, in context

	'''

	polls = Poll.objects.all()
	choices = Choice.objects.all()
	context = {
	
	"polls": polls, "choices": choices
	
	}
	return render(request, "polls/polls_list.html", context)

def poll_detail(request, poll_id):
	#return HttpResponse(f'<h1> you are looking for a poll with an id of {poll_id}</h1>')



	#poll = Poll.objects.get(id=poll_id)
	poll = get_object_or_404(Poll, id=poll_id)
	context = {
	'poll': poll
	}



	return render(request, 'polls/poll_detail.html', context )



# Create your views here.
