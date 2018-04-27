from django import forms
from passes.serializers import PassSerializer
from passes.models import Pass


COLOR_CHOICES= [
        ('-1', 'Pick a color for this pass'),
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
        ('10', 'Green'),
    ]

class PassForm(forms.Form):
    target = forms.CharField(
        label='NetId', 
        max_length=100
    )
    source = forms.CharField(
        max_length=50, 
        widget=forms.HiddenInput()
    )
    transferrable = forms.BooleanField()
    # passId = forms.CharField(max_length=50, widget=forms.HiddenInput())

class ActivateForm(forms.Form):
    pass_id = forms.IntegerField(min_value=0)

class MultipleForm(forms.Form):
    action = forms.CharField(
        max_length=60, 
        widget=forms.HiddenInput()
    )

class AddOfficerForm(MultipleForm):
    target = forms.CharField(
        label='NetId', 
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                'class':'form-control col-sm-8 admin-hmpg-form-input'
            }
        )
    )
    source = forms.CharField(
        max_length=50, 
        widget=forms.HiddenInput()
    )

class MakePassForm(MultipleForm):
    pass_date = forms.DateField(
        label='Date',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control datetime-input col-sm-8 admin-hmpg-form-input',
                'placeholder': 'What date should this pass be used on?'
            }
        )
    )
    color = forms.CharField(
        label='Color', 
        widget=forms.Select(
            choices=COLOR_CHOICES, 
            attrs={
                'class': 'form-control col-sm-8 admin-hmpg-form-input',
                'placeholder': 'What color should this pass be?'
            }
        )
    )
    number = forms.IntegerField(
        label='Count', 
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control col-sm-8 admin-hmpg-form-input',
                'placeholder': 'Number of passes each member will receive.'
            }
        )
    )
    transferrable = forms.BooleanField(
        label='Transferable:', 
        initial=True,
        disabled=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control admin-hmpg-form-checkbox',
            }
        )
    )
    source = forms.CharField(
        max_length=50, 
        widget=forms.HiddenInput()
    )
