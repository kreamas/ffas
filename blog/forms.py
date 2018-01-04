# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 07:51:23 2017

@author: alexkreamas
"""

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
        
class Nombre(forms.Form):
    miNombre = forms.CharField(label = 'Tu nombre', max_length=100)
    
class eligeNombre(forms.Form)    :
    FILTER_CHOICES = (
        ('time', 'Time'),
        ('timesince', 'Time Since'),
        ('timeuntil', 'Time Untill'),
    )

    filter_by = forms.ChoiceField(label = 'Elige tu nombre', choices=FILTER_CHOICES)
    
class eligeNombreZ(forms.Form)    :
    FILTER_CHOICES = (
        ('calef', 'Calef'),
        ('alex', 'Alex'),
        ('ivan', 'Ivan'),
    )

    filtro = forms.MultipleChoiceField(label = 'Elige tu nombre', choices=FILTER_CHOICES)
    