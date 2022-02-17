
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice
from django.shortcuts import render, get_object_or_404

# function based views
# class based views


class IndexView(generic.ListView):
    # template_name = 'polls/question_list.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    # template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/question_detail.html', {
            'question': question,
            'error_message': 'Você deve escolher uma opção.'
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,)
        ))
