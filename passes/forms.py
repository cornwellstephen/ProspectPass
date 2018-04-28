from django import forms
from passes.serializers import PassSerializer
from passes.models import Pass, Student


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

NETID = ''

def setNetId(netid):
    global NETID
    NETID = netid

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
    def __init__(self, *args, **kwargs):
        self.netid = kwargs.pop("netid", None)
        super(MultipleForm, self).__init__(*args, **kwargs)
        setNetId(self.netid)
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
class SingleDist(MultipleForm):
    
    # def get_passes(user_netid):
    #     PASS_CHOICES = []
    #     officer = Student.objects.all().filter(NetId=user_netid)[0]
    #     for _pass in officer.passes.all():
    #         if _pass.club_name == officer.user_club:
    #             PASS_CHOICES.append((_pass.pk, _pass.pass_date))
    #     return PASS_CHOICES
    passes = forms.CharField(
        # queryset = Student.objects.all().filter(NetId=NETID),
        label='Pass', 
        widget=forms.Select(
            attrs={
                'class': 'form-control col-sm-8 admin-hmpg-form-input',
                'placeholder': 'What color should this pass be?'
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

    def __init__(self, *args, **kwargs):
        super(SingleDist, self).__init__(*args, **kwargs)
        self.pass_choices = []
        officer = Student.objects.all().filter(NetId=NETID)[0]
        for _pass in officer.passes.all():
            if _pass.club_name == officer.user_club:
                self.pass_choices.append((_pass.pk, _pass.pass_date))
        self.fields['passes'].widget.choices = self.pass_choices

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
    source = forms.CharField(
        max_length=50, 
        widget=forms.HiddenInput()
    )

class UploadFileForm(MultipleForm):
    file = forms.FileField()
    source = forms.CharField(max_length=50, widget=forms.HiddenInput())
