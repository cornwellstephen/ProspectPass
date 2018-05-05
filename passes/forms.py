from django import forms
from passes.serializers import PassSerializer
from passes.models import Pass, Student
from django.utils.timezone import datetime


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
        max_length=100,
    )
    source = forms.CharField(
        max_length=50, 
        widget=forms.HiddenInput()
    )
    transferrable = forms.BooleanField(required=False)
    # passId = forms.CharField(max_length=50, widget=forms.HiddenInput())

    def clean_target(self):
        target = self.cleaned_data['target']
        if len(Student.objects.all().filter(NetId=target)) == 0:
            raise forms.ValidationError("You have inputted an invalid NetId.")
        return target

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
        ),
        required=False
    )
    source = forms.CharField(
        max_length=50, 
        widget=forms.HiddenInput(),
    )

    def clean_target(self):
        target = self.cleaned_data['target']
        print(target)
        if target == None or len(Student.objects.all().filter(NetId=target)) == 0:
            raise forms.ValidationError("You have inputted an invalid NetId.")
        else: # check if already officer
            student = Student.objects.all().filter(NetId=target)[0]
            if student.officer_status == True:
                raise forms.ValidationError("This person is already an officer.")
        return target


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
                'placeholder': 'What pass do you want to send?'
            }
        ),
        required=False
    )
    transferrable = forms.BooleanField(
        label='Transferable:', 
        initial=True,
        disabled=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control admin-hmpg-form-checkbox',
            }
        ),
        required=False
    )        
    person = forms.CharField(
        label='NetId', 
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                'class':'form-control col-sm-8 admin-hmpg-form-input'
            }
        ),
        required=False
    )
    number = forms.IntegerField(
        label='Count', 
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control col-sm-8 admin-hmpg-form-input',
                'placeholder': 'Number of passes the member will receive.'
            }
        ),
        required=False
    )
    source = forms.CharField(
        max_length=50, 
        widget=forms.HiddenInput()
    )
    def clean_person(self):
        target = self.cleaned_data['person']
        if len(Student.objects.all().filter(NetId=target)) == 0:
            raise forms.ValidationError("You have inputted an invalid NetId.")
        return target

    def clean_number(self):
        number = self.cleaned_data['number']
        if number is None:
            raise forms.ValidationError("You must select a positive number of passes")
        return number

    def clean_pass(self):
        _pass = self.cleaned_data['pass']
        if _pass is None:
            raise forms.ValidationError("You must select a pass")
        return _pass

    def __init__(self, *args, **kwargs):
        super(SingleDist, self).__init__(*args, **kwargs)
        self.pass_choices = []
        officer = Student.objects.all().filter(NetId=NETID)[0]
        for _pass in officer.passes.all():
            if _pass.club_name == officer.user_club and _pass.pass_date >= datetime.today().date():
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
        ),
        required=False
    )
    color = forms.CharField(
        label='Color', 
        widget=forms.Select(
            choices=COLOR_CHOICES, 
            attrs={
                'class': 'form-control col-sm-8 admin-hmpg-form-input',
                'placeholder': 'What color should this pass be?'
            }
        ),
        required=False
    )
    number_pass = forms.IntegerField(
        label='Count', 
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control col-sm-8 admin-hmpg-form-input',
                'placeholder': 'Number of passes each member will receive.'
            }
        ),
        required=False
    )
    source = forms.CharField(
        max_length=50, 
        widget=forms.HiddenInput()
    )

    def clean_pass_date(self):
        pass_date = self.cleaned_data['pass_date']
        if pass_date == None:
            raise forms.ValidationError("You must select a valid date")
        elif pass_date < datetime.today().date():
            raise forms.ValidationError("You must select a date that's not in the past")
        return pass_date

    def clean_number_pass(self):
        number = self.cleaned_data['number_pass']
        if number is None:
            raise forms.ValidationError("You must select a positive number of passes")
        return number

class UploadFileForm(MultipleForm):
    file = forms.FileField(required=False)
    source = forms.CharField(max_length=50, widget=forms.HiddenInput(), required=False)

    def clean_file(self):
        _pass = self.cleaned_data['file']
        if _pass is None:
            raise forms.ValidationError("You must upload a valid file")
        return _pass
