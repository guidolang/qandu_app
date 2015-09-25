from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
class QuestionCreateView(CreateView):
    model = Question
    template_name = 'question/question_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('question_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(QuestionCreateView, self).form_valid(form)
    
class QuestionListView(ListView):
    model = Question
    template_name = 'question/question_list.html'
    
class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question/question_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        question = Question.objects.get(id=self.kwargs['pk'])
        answers = Answer.objects.filter(question=question)
        context['answers'] = answers
        return context
    
class QuestionUpdateView(UpdateView):
    model = Question
    template_name = 'question/question_form.html'
    fields = ['title', 'description']
    
    def get_object(self, *args, **kwargs):
        object = super(QuestionUpdateView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object
    
class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'question/question_confirm_delete.html'
    success_url = reverse_lazy('question_list')
    
    def get_object(self, *args, **kwargs):
        object = super(QuestionDeleteView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object
    
class AnswerCreateView(CreateView):
    model = Answer
    template_name = 'answer/answer_form.html'
    fields = ['text']
    
    def get_success_url(self):
        return self.object.question.get_absolute_url()
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question = Question.objects.get(id=self.kwargs['pk'])
        return super(AnswerCreateView, self).form_valid(form)
    
class AnswerUpdateView(UpdateView):
    model = Answer
    pk_url_kwarg = 'answer_pk'
    template_name = 'answer/answer_form.html'
    fields = ['text']
    
    def get_success_url(self):
        return self.object.question.get_absolute_url()
    
    def get_object(self, *args, **kwargs):
        object = super(AnswerUpdateView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class AnswerDeleteView(DeleteView):
    model = Answer
    pk_url_kwarg = 'answer_pk'
    template_name = 'answer/answer_confirm_delete.html'
    
    def get_success_url(self):
        return self.object.question.get_absolute_url()
    
    def get_object(self, *args, **kwargs):
        object = super(AnswerDeleteView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object
    