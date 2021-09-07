from django import forms
from django.forms import fields

from .models import Todo, User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'profile_pic']

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            'task',
            'description',
            'bydate',
            'bytime'
        ]
        widgets = {
            'bydate': forms.DateInput(attrs={'type':'date'}),
            'bytime': forms.TimeInput(attrs={'type':'time'})
        }

# class TodoForm(forms.Form):
#     task        = forms.CharField()
#     description = forms.CharField()
#     bydate      = forms.DateField(widget=DateInput)
#     bytime      = forms.TimeField(widget=TimeInput)
