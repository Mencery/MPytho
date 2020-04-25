from django import forms
from .models import *


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question"]
        exclude = ["id"]


class AddAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["answer"]
