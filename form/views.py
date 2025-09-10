from django.shortcuts import render, get_object_or_404
from django.views import View, generic
from .models import Question
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
class QuestionView(View):
    def get(self, request):
        return render(request, 'form/question_view.html', {'question_list' : Question.objects.all().values()})


class QuestionDetalView(View):
    def get(self, request, question_id):
        selected_question = get_object_or_404(Question, pk=question_id)
        choice_list = selected_question.choice_set.all()
        return render(request, 'form/question_detail_view.html', {'selected_question' : selected_question, 'choice_list' : choice_list})
    
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            choice_id = request.POST.get('choice')
            selected_choice = question.choice_set.get(pk=choice_id)

        except(Exception):
            error = False
            return render(request, 'form/question_detail_view.html', {'error' : error})
        
        else:
            if(not selected_choice is None):
                selected_choice.vote += 1
                selected_choice.save()
            return HttpResponseRedirect(reverse('form:vote_question_view', args=(question.id,)))


class VoteQuestionView(View):
    def get(self, request, question_id):
        return render(request, 'form/vote_question_view.html', {'question' : get_object_or_404(Question, pk=question_id)})