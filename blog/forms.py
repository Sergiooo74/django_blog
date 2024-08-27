from django import forms
from .models import Post

# class PostForm(forms.Form):
#     author = forms.CharField(max_length=50, label="Author")
#     title = forms.CharField(max_length=200, label="Title")
#     text = forms.CharField(label='Post text', widget=forms.Textarea())

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'image']
