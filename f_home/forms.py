from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Post, LanguageStack
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _


class TechForm(ModelForm):
    class Meta:
        model = LanguageStack
        fields = ('title',) 
        labels = { 'title': _('Language/Technology'),}

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'estd', 'size', 'address', 'websitelink','tech', 'logo')
        labels = {
            'name': _('Company Name'),
            'estd': _('Established Year'), 
            'size': _('Approx Employee'),
            'address': _('Company Address'),
            'websitelink': _('Company Website Link'),
            'tech': _('Technology Use'),
            'logo': _('Company Logo'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TechStack Ltd.'}),
            'estd': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1901'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'House #, Road #, Block #, Xyz Area, Dhaka- ####'}),
            'websitelink': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://www.techstack.com'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['size'].empty_label = "Select Employee"