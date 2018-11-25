from django.shortcuts import render
from django.http import HttpResponse



def polls_list(request):

	context = {

	}
	return render(request, "polls/polls_list.html", context)
# Create your views here.
