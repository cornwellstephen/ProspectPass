from django import forms
from passes.serializers import PassSerializer
from passes.models import Pass, Student
from django.utils.timezone import datetime
from django.http import HttpResponseRedirect

COLOR_CHOICES= [
        ('8', '#e5e358'),
        ('1', '#e9b000'),
        ('0', '#e24e42'),
        ('7', '#ee3377'),
        ('2', '#eb6e80'),
        ('4', '#94618e'),
        ('6', '#273f5f'),
        ('3', '#008f95'),
        ('9', '#a7d2cb'),
        ('5', '#8fd8f2'),
        ('10', '#11895a'),  
    ]

NETID = ''

MAX_UPLOAD_SIZE = 5242880

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
                'class':'form-control admin-hmpg-form-input'
            }
        ),
        required=True
    )
    source = forms.CharField(
        max_length=50, 
        widget=forms.HiddenInput(),
    )

    def clean_target(self):
        target = self.cleaned_data['target'].lower().strip()
        if target == None or len(Student.objects.all().filter(NetId=target)) == 0:
            return "person_wrong"
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
                'class': 'form-control admin-hmpg-form-input',
                'placeholder': 'What pass do you want to send?'
            }
        ),
        required=False
    )
    transferrable = forms.BooleanField(
        label='Transferable:', 
        initial=True,
        disabled=True,
        widget=forms.HiddenInput(
            attrs={
                'class': 'form-control admin-hmpg-form-checkbox',
            }
        ),
        required=False,
    )        
    person = forms.CharField(
        label='NetId', 
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                'class':'form-control admin-hmpg-form-input'
            }
        ),
        required=True
    )
    number = forms.IntegerField(
        label='Count', 
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control admin-hmpg-form-input',
                'placeholder': 'Number of passes the student will receive.'
            }
        ),
        required=True
    )
    source = forms.CharField(
        max_length=50, 
        widget=forms.HiddenInput()
    )
    def clean_person(self):
        target = self.cleaned_data['person'].lower().strip()
        if len(Student.objects.all().filter(NetId=target)) == 0:
            return "person_wrong"
        return target

    def clean_number(self):
        number = self.cleaned_data['number']
        if number is None:
            return "number_wrong"
        return number

    def clean_passes(self):
        _pass = self.cleaned_data['passes']
        if _pass is None or _pass == "":
            return "pass_wrong"
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
                'class': 'form-control datetime-input admin-hmpg-form-input',
                'placeholder': 'What date should this pass be used on?'
            }
        ),
        required=True
    )
    color = forms.CharField(
        label='Pick a color for this pass:', 
        widget=forms.RadioSelect(
            choices=COLOR_CHOICES, 
            attrs={
                'class': 'admin-hmpg-form-radios',
                'placeholder': 'What color should this pass be?'
            }
        ),
        required=True
    )
    number_pass = forms.IntegerField(
        label='Count', 
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control admin-hmpg-form-input',
                'placeholder': 'Number of passes each member will receive.'
            }
        ),
        required=True
    )
    source = forms.CharField(
        max_length=50, 
        widget=forms.HiddenInput()
    )

    def clean_pass_date(self):
        pass_date = self.cleaned_data['pass_date']
        if pass_date == None:
            return "date_wrong"
        elif pass_date < datetime.today().date():
            return "date_wrong"
        return pass_date

    def clean_number_pass(self):
        number = self.cleaned_data['number_pass']
        if number is None:
            return "number_wrong"
        return number


class UploadFileForm(MultipleForm):
    file = forms.FileField(required=True)
    source = forms.CharField(
        max_length=50, 
        widget=forms.HiddenInput(), 
        required=False
    )

    def clean_file(self):
        file = self.cleaned_data['file']
        if file is None:
            return "upload_fail"
        elif not file.name.endswith('.csv'):
            return "upload_fail"
        elif file._size > MAX_UPLOAD_SIZE:
            return "upload_size_fail"
        return file
