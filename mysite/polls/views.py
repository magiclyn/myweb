from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .forms import NameForm
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')#[:5]
# 	template = loader.get_template('polls/index.html')
# 	context = {'latest_question_list':latest_question_list}
# 	return HttpResponse(template.render(context,request))


# def detail(request,question_id):
# 	question = get_object_or_404(Question,pk=question_id)
# 	return render(request,'polls/detail.html',{'question':question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	print(question_id)
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail',{'question':question,'error_message':"You didn't select a choice."})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# return HttpResponse(reverse('polls:results',args=(question.id,)))
		# return render(request,'polls/results.html',{'question':question})
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,))) 


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    queryset =  Question.objects.order_by('-pub_date')
    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]
		
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'




def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            return HttpResponse('hiiiiiiiiiiiiiiii')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'polls/getName.html', {'form': form})


		
		