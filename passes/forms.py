from django import forms

class PassForm(forms.Form):
    target = forms.CharField(label='NetId', max_length=100)
