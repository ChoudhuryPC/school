from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from ..decorators import teacher_required
from ..forms import TeacherSignUpForm
from ..models import Quiz, User,Answer
from ..cron import check

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teachers:quiz_change_list')


@method_decorator([login_required, teacher_required], name='dispatch')
class QuizListView(ListView):
    model = Quiz
    ordering = ('name', )
    context_object_name = 'quizzes'
    template_name = 'classroom/teachers/quiz_change_list.html'

    def get_queryset(self):
        queryset = self.request.user.quizzes \
            .select_related('subject') 
        return queryset


@method_decorator([login_required, teacher_required], name='dispatch')
class QuizCreateView(CreateView):
    model = Quiz
    fields = ('name', 'subject', 'pdf','date','start','end',)
    labels = {
        "name":"SUBJECT NAME",
        "pdf":"UPLOAD QUESTION PAPER",
        "date":"DATE OF EXAM",
        "start":"EXAM START TIME",
        "end":"EXAM END TIME",
        "subject": "CLASS"}
    template_name = 'classroom/teachers/quiz_add_form.html'

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.owner = self.request.user
        quiz.save()
        messages.success(self.request, 'The quiz was created with success! Go ahead and add some questions now.')
        return redirect('teachers:quiz_change', quiz.pk)


@method_decorator([login_required, teacher_required], name='dispatch')
class QuizUpdateView(UpdateView):
    model = Quiz
    fields = ('name', 'subject', 'pdf','date','start','end',)
    labels = {
        "name":"SUBJECT NAME",
        "pdf":"UPLOAD QUESTION PAPER",
        "date":"DATE OF EXAM",
        "start":"EXAM START TIME",
        "end":"EXAM END TIME",
        "subject": "CLASS"
        

        }
    context_object_name = 'quiz'
    template_name = 'classroom/teachers/quiz_change_form.html'

    def get_queryset(self):
        '''
        This method is an implicit object-level permission management
        This view will only match the ids of existing quizzes that belongs
        to the logged in user.
        '''
        return self.request.user.quizzes.all()

    def get_success_url(self):
        return reverse('teachers:quiz_change', kwargs={'pk': self.object.pk})


@method_decorator([login_required, teacher_required], name='dispatch')
class QuizDeleteView(DeleteView):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'classroom/teachers/quiz_delete_confirm.html'
    success_url = reverse_lazy('teachers:quiz_change_list')

    def delete(self, request, *args, **kwargs):
        quiz = self.get_object()
        messages.success(request, 'The quiz %s was deleted with success!' % quiz.name)
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.quizzes.all()



@method_decorator([login_required, teacher_required], name='dispatch')
class AnswerListView(ListView):
    model = Answer
    ordering = ('section','roll','subject', )
    context_object_name='answers'
    template_name = 'classroom/teachers/quiz_answers.html'



@method_decorator([login_required, teacher_required], name='dispatch')
class Class1(ListView):
    model = Answer
    ordering = ('section','roll','subject', )
    context_object_name='answers'
    template_name = 'classroom/teachers/class1.html'
