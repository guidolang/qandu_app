from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
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
    
class QuestionUpdateView(UpdateView):
    model = Question
    template_name = 'question/question_form.html'
    fields = ['title', 'description']
    
class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'question/question_confirm_delete.html'
    success_url = reverse_lazy('question_list')