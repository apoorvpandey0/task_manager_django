from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import TodoItem

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title','description','priority','completed']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter todo title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter todo description',
                }
            ),
            'priority': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter todo priority',
                }
            ),
            'completed': forms.CheckboxInput(
                attrs={
                    
                    
                }
            ),

        }
