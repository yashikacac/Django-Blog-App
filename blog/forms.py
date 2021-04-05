from django import forms

from .models import Post
from .forms import PostForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)