from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    #file = forms.FileField(required=False)
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'file')
        widgets = {
            'title': forms.TextInput(),
            'author': forms.TextInput(),
            'body': forms.Textarea(),
            'file': forms.FileField(),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'file')
        widgets = {
            'title': forms.TextInput(),
            'body': forms.Textarea(),
            'file': forms.FileField(),
        }

