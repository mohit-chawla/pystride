from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import render

from django.template import loader

from .models import Question

def index(request):
	#writing view shere
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# output = ','.join([q.question for q in latest_question_list])
	# return HttpResponse(output)
	#need a template for flexibity
	template = loader.get_template('polls/index.html')
	context ={
	'latest_question_list' : latest_question_list,
	} 
	return HttpResponse(template.render(context,request))

	##SHORTCUT
	#    return render(request, 'polls/index.html', context)


def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	#method 1 sending static http response
	# return HttpResponse("You are looking at question %s" %question_id)
	#method 2 using hardcoded templates
	return render(request,'polls/detail.html',{'question': question})

def results(request,question_id):
	response = "You are looking at results of question %s" 
	return HttpResponse(response %question_id)

def vote(request, question_id):
	return HttpResponse("You are voting for question %s" %question_id)