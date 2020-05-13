from .models import Post, Usuario
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin.widgets import AdminTimeWidget
import datetime
import django

class PostForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=250, required=True)
    paragraph = forms.CharField(label="Paragraph", max_length=250, required=True)
    image = forms.FileField(label="Image", required=False)
    

    class Meta:
        db_table = "post"
        model = Post
        fields = ("title",  "date","paragraph", "image")
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['disabled'] = 'disabled'
        self.fields['date'].required = False
    def clean_type(self):
        if self.instance and self.instance.pk:
            return self.instance.date
        else:
            return self.cleaned_data['date']

class SignInForm(forms.Form):
    """
    Iniciar sesión
    """
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(label='Contraseña')
