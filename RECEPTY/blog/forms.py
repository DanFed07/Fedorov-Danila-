from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import News, Article, Comment

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок статьи', 'style': 'width: 100%; padding: 0.5rem;'}),
            'content': forms.Textarea(attrs={'rows': 15, 'class': 'form-control', 'placeholder': 'Содержание статьи', 'style': 'width: 100%; padding: 0.5rem;'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'example@mail.ru'}))
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Анна Иванова'}))

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'username'})
        self.fields['password1'].widget.attrs.update({'placeholder': '••••••••'})
        self.fields['password2'].widget.attrs.update({'placeholder': '••••••••'})

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '••••••••'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Напишите ваш комментарий...'}),
        }

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image', 'is_main']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
            'content': forms.Textarea(attrs={'rows': 10, 'class': 'form-control', 'placeholder': 'Содержание новости'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок статьи'}),
            'content': forms.Textarea(attrs={'rows': 15, 'class': 'form-control', 'placeholder': 'Содержание статьи'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }