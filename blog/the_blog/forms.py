from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'image')

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs = {'class': 'form-control'}),
            'author': forms.TextInput(attrs = {'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'category': forms.Select(choices = choices, attrs = {'class': 'form-control'}),
            'body': forms.Textarea(attrs = {'class': 'form-control'}),
            'snippet': forms.Textarea(attrs = {'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs = {'class': 'form-control'}),
            'body': forms.Textarea(attrs = {'class': 'form-control'}),
            'snippet': forms.Textarea(attrs = {'class': 'form-control'}),
        }