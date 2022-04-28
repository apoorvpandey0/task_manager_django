from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = '__all__'

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
