from django import forms
from tasks.models import Task, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category', 'description', 'due_date', 'priority']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Купить хлеба'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), # type="date" включит календарь
            'category': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'title': 'Заголовок',
            'category': 'Категория',
            'description': 'Описание',
            'due_date': 'Срок выполнения',
            'priority': 'Приоритет',
        }
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username'] 