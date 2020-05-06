from django import forms
from .models import Post
import datetime
from django.contrib.admin.widgets import AdminTimeWidget

class PostForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=250, required=True)
    #date = forms.DateField(initial=datetime.date.today, widget=AdminTimeWidget(format=' %H:%M:%S'));
    paragraph = forms.CharField(label="Paragraph", max_length=250, required=False)
    image = forms.FileField(label="Image", required=False)
    

    class Meta:
        db_table = "post"
        model = Post
        fields = ("title",  "date","paragraph", "image")
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['disabled'] = 'disabled'
        
