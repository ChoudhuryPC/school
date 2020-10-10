from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from django import forms
from ..decorators import student_required
from ..forms import StudentInterestsForm, StudentSignUpForm,AnswerForm
from ..models import Quiz, Student,User,Answer
from django.views.generic import TemplateView
from ..cron import check
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students:quiz_list')


@method_decorator([login_required, student_required], name='dispatch')
class StudentInterestsView(UpdateView):
    model = Student
    form_class = StudentInterestsForm
    template_name = 'classroom/students/interests_form.html'
    success_url = reverse_lazy('students:quiz_list')

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, 'Interests updated with success!')
        return super().form_valid(form)


@method_decorator([login_required, student_required], name='dispatch')
class QuizListView(ListView):
    model = Quiz
    ordering = ('date', )
    context_object_name = 'quizzes'
    check()

    template_name = 'classroom/students/quiz_list.html'

    def get_queryset(self):
        student = self.request.user.student
        student_interests = student.interests.values_list('pk', flat=True)
        queryset = Quiz.objects.filter(subject__in=student_interests)
        return queryset





class ThanksView(TemplateView):
    template_name = 'classroom/students/quiz_thankyou.html'

@method_decorator([login_required, student_required], name='dispatch')
class AnswerCreateForm(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'classroom/students/answer_form.html'
    success_url = reverse_lazy('students:thanks')

       




        




