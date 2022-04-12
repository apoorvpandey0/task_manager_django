from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'rounded text-sm py-2 px-4 ',
                    'placeholder': 'Enter todo title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'rounded text-sm py-2 px-4',
                    'placeholder': 'Enter todo description',
                }
            ),
            'priority': forms.NumberInput(
                attrs={
                    'class': 'rounded text-sm py-2 px-4',
                    'placeholder': 'Enter todo priority',
                }
            ),
            'completed': forms.CheckboxInput(
                attrs={
                    'class': 'text-sm py-2 px-4',
                    
                }
            ),

        }
