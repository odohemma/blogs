from django import forms
from django.forms import ModelForm, fields
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'tags','source_link','demo_link', 'author']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kvargs):
        super(ProjectForm, self).__init__(*args, **kvargs)

        # self.fields['title'].widget.attrs.update({'class': 'input'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input',  'placeholder':"Enter text"})