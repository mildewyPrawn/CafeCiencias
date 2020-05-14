from .models import Post, Usuario
from django import forms
from django.contrib.admin.widgets import AdminTimeWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django.forms import ValidationError
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

class CreateUrs(UserCreationForm):
    
    nombre = forms.CharField(max_length=64)
    paterno = forms.CharField(max_length=100)
    
    field_order = ['nombre', 'paterno', 'email', 'password1', 'password2']

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', )


    def save(self, commit=True):
        username = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('nombre')
        last_name = self.cleaned_data.get('paterno')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')
        user = User.objects.create_user(username=email, first_name=first_name,
                                        last_name=last_name,
                                        email=email, password=password)
        if commit:
            pass
        return user
    
    def clean_email(self):
        # Valida que el correo no exista en la base de datos
        data = self.cleaned_data.get('email')
        if User.objects.filter(email=data).count() > 0:
            raise forms.ValidationError("Este correo ya está registrado")
        # Valida que termine con unam.mx
        if not data.endswith('unam.mx'):
            raise ValidationError('El dominio no es valido.')
        return data
