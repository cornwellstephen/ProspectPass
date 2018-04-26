from django import forms
from passes.serializers import PassSerializer
from passes.models import Pass


COLOR_CHOICES= [
    ('0', 'Red'),
    ('1', 'Yellow'),
    ('2', 'Pink'),
    ('3', 'Turqoise'),
    ('4', 'Purple'),
    ('5', 'Light Blue'),
    ('6', 'Dark Blue'),
    ('7', 'Bright Pink'),
    ('8', 'Bright Green'),
    ('9', 'Super Light Blue'),
    ]

class PassForm(forms.Form):
    target = forms.CharField(label='NetId', max_length=100)
    source = forms.CharField(max_length=50, widget=forms.HiddenInput())
    # passId = forms.CharField(max_length=50, widget=forms.HiddenInput())

class ActivateForm(forms.Form):
	pass_id = forms.IntegerField(min_value=0)

class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class AddOfficerForm(MultipleForm):
	target = forms.CharField(label='NetId', max_length=100)
	source = forms.CharField(max_length=50, widget=forms.HiddenInput())

class MakePassForm(MultipleForm):
	pass_date = forms.DateField(widget=forms.TextInput(attrs=
                    {
                        'class':'datetime-input'
                    }))
	color = forms.CharField(label='What is the pass color?', widget=forms.Select(choices=COLOR_CHOICES))
	number = forms.IntegerField(label='Number of passes', min_value=0)
	transferrable = forms.BooleanField(label='Transferrable?')
	source = forms.CharField(max_length=50, widget=forms.HiddenInput())
