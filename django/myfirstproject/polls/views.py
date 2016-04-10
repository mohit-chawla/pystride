from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.template import loader

from django.core.urlresolvers import reverse

from .models import Question, Choice

#view for home
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


#view for each question's voting page
def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	#method 1 sending static http response
	# return HttpResponse("You are looking at question %s" %question_id)
	#method 2 using hardcoded templates
	return render(request,'polls/detail.html',{'question': question})

#view to see results of a particular question
def results(request,question_id):
	# response = "You are looking at results of question %s" 
	# return HttpResponse(response %question_id)
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

#function handling POST submissions of a vote from detail.html
def vote(request, question_id):
	# return HttpResponse("You are voting for question %s" %question_id)
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk =request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# redisplay the question voting form
		return render(request, 'polls/detail.html', {
			question : question,
			error_message : 'You did not select a choice'
			})

	else:
		this_question = Question.objects.get(pk=question_id)
		this_question.total_responses +=1
		this_question.save()
		selected_choice.votes +=1
		selected_choice.save()
		# return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # reverse() function in HttpResponseRedirect constructor is used to avoid having to hardcode URL
        # return control to results view

#see most-responded questions and trending questions
def trending(request):
	#get top 3 trending polls here
	trending_questions_list =  Question.objects.order_by('-total_responses')[:3]
	#retuirn trending polls to the user
	return render(request,'polls/trending.html',{'list' : trending_questions_list})

