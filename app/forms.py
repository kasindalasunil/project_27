from django import forms

from app.models import *

def validate_for_s(data):
    if data.lower().startswith('s'):
        raise forms.ValidationError('invalid data')
def validate_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('invalid data')
    



class SchoolForm(forms.Form):
    sname=forms.CharField(validators=[validate_for_s, validate_for_len])
    sprincipal=forms.CharField(validators=[validate_for_len])
    slocation=forms.CharField()
    email=forms.EmailField()
    reenteremail=forms.EmailField()

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reenteremail']

        if e!=re:
            raise forms.ValidationError('invalid data')

    