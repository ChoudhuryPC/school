from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from classroom.models import (Student,
                              Subject, User,Quiz,Answer)


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields=('username','email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user


class StudentSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    def clean_interests(self):
        value=self.cleaned_data['interests']
        if len(value)>1:
            raise forms.ValidationError("Please select one class only !")
        return value

    class Meta(UserCreationForm.Meta):
        model = User
        fields=('username','email')
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user


class StudentInterestsForm(forms.ModelForm):
    def clean_interests(self):
        value=self.cleaned_data['interests']
        if len(value)>1:
            raise forms.ValidationError("Please select one class only !")
        return value


    class Meta:
        model = Student
        fields = ('interests', )
        widgets = {
            'interests': forms.CheckboxSelectMultiple
        }
        labels={
        "interests" : "CLASS",
        }


class AnswerForm(forms.ModelForm):
    """docstring for AnswerForm"""
    answer=forms.FileInput()
    
    class Meta():
        model=Answer
        fields=('subject','quiz_name','section','roll','answer',)
        labels = {
        "subject": "CLASS",
        "quiz_name": "SUBJECT NAME",
        "roll":"ROLL",
        "section":"SECTION"

        }
        
        


    
