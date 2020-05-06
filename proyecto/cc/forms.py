from django import forms
from .models import Post
import datetime
from django.contrib.admin.widgets import AdminTimeWidget
import django
class PostForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=250, required=True)
    #date = forms.DateField(disabled =True, default=django.utils.timezone.now);
    paragraph = forms.CharField(label="Paragraph", max_length=250, required=False)
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
