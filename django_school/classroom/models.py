from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.utils import timezone
from datetime import datetime
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255,help_text="SUBJECT NAME")
    pdf = models.FileField(upload_to='teacher',blank=False,default='teacher/default.jpg')
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    today = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    start = models.TimeField(auto_now=False,blank=True,auto_now_add=False,help_text="Enter time in 24 hour format !")
    end = models.TimeField(auto_now=False,blank=True,auto_now_add=False,help_text="Enter time in 24 hour format !")
    current_time = datetime.now().strftime("%H:%M")
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes',help_text="Select CLASS")

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    interests = models.ManyToManyField(Subject, related_name='interested_students')

    def __str__(self):
        return self.user.username


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()

class Answer(models.Model):
    """docstring for Answer"""
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='subject_fill',default=1)
    roll = models.PositiveIntegerField(default=1)
    quiz_name = models.CharField(max_length=20,default='ENTER SUBJECT')
    answer = models.FileField(upload_to='student',blank=False,default='teacher/default.jpg')
    section = models.CharField(max_length=1,default="A")

    def __str__(self):
        return self.quiz_name 

    def save(self, force_insert=False, force_update=False):
        self.quiz_name = self.quiz_name.upper()
        super(Answer, self).save(force_insert, force_update)

    def save(self, force_insert=False, force_update=False):
        self.section = self.section.upper()
        super(Answer, self).save(force_insert, force_update)

    def get_absolute_url(self):
        return reverse('teachers:quiz_answers',kwargs={'pk':self.pk})

    