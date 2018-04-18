from django import forms
from passes.serializers import PassSerializer
from passes.models import Pass


class PassForm(forms.Form):
    target = forms.CharField(label='NetId', max_length=100)
    source = forms.CharField(max_length=50, widget=forms.HiddenInput())
    # passId = forms.CharField(max_length=50, widget=forms.HiddenInput())
