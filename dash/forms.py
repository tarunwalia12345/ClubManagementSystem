from django.core import validators
from django.db import models 
from django import forms
from .models import Form
class ReqForm(forms.ModelForm):
    class Meta:
        model=Form
        fields=['email','ClubName','RepresentativeName','Contact','req_date_from','req_date_to','req_type','req_purpose']
        help_text={'email':'enter email in abc@xyz.com format'}
class mess(forms.ModelForm):
    class Meta:
        model=Form
        fields=['Management_Comments']
        
