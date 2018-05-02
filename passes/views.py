from django.shortcuts import render

from rest_framework import permissions, viewsets

from passes.models import Student, Pass
from passes.permissions import IsStudentOwner
from passes.serializers import StudentSerializer, PassSerializer

from django.views import generic
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .forms import PassForm, AddOfficerForm, MakePassForm, ActivateForm, UploadFileForm, SingleDist
from django.http import HttpResponseRedirect
from .multiforms import MultiFormsView
from django.urls import reverse, reverse_lazy
import json
from rest_framework import filters
# Create your views here.
class Index(generic.ListView):
	template_name = 'index.html'

	def get_queryset(self):
		return

class Homepage(LoginRequiredMixin, generic.ListView):
	template_name = 'homepage.html'
	login_url = 'login/'
	raise_exception = False
	def get_queryset(self):
		return

class AdminHomepage(LoginRequiredMixin, generic.ListView):
    template_name = 'admin-homepage.html'
    login_url = 'login/'
    raise_exception = False
    def get_queryset(self):
        return

class StudentViewSet(viewsets.ModelViewSet):
    lookup_field = 'NetId'
    serializer_class = StudentSerializer
    def get_queryset(self):
            return Student.objects.all()

class PassViewSet(viewsets.ModelViewSet):
	queryset = Pass.objects.all()
	serializer_class = PassSerializer

class SentPass(generic.ListView):
    template_name = 'sentpass.html'
    def get_queryset(self):
        return

class AddedOfficer(generic.ListView):
    template_name = 'addedofficer.html'
    def get_queryset(self):
        return

class FileUploaded(generic.ListView):
    template_name = 'fileuploaded.html'
    def get_queryset(self):
        return

class OfficerAlreadyAdded(generic.ListView):
    template_name = 'officer-already-added.html'
    def get_queryset(self):
        return

class MadePass(generic.ListView):
    template_name = 'madepass.html'
    def get_queryset(self):
        return

class Distributed(generic.ListView):
    template_name = 'distributed.html'
    def get_queryset(self):
        return

def send_pass(request, pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PassForm(json.loads(request.body.decode('utf-8')))
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            netid = form.cleaned_data['target']
            source = form.cleaned_data['source']
            transferrable = form.cleaned_data['transferrable']
            # passId = form.cleaned_data['passId']
            source_user = Student.objects.all().filter(NetId=source)[0]
            target_pass = Pass.objects.all().filter(pk=pk)[0]
            if source_user.officer_status is True and source_user.user_club == target_pass.club_name:
                source_user.officerDirectSend(target_pass, netid, transferrable)
            else:
                source_user.sendpass(target_pass, netid, transferrable)
            return HttpResponseRedirect('/sentpass')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PassForm()

    return render(request, 'homepage.html', {'form': form})

def activate_pass(request):
    if request.method == 'POST':
        form = ActivateForm(json.loads(request.body.decode('utf-8')))
        if form.is_valid():
            pass_id = form.cleaned_data['pass_id']
            target_pass = Pass.objects.all().filter(pk=pass_id)[0]
            target_pass.activated = True
            target_pass.save()
            return HttpResponseRedirect('/homepage/')
    else:
        form = ActivateForm()
    return render(request, 'homepage.html', {'form': form})

class MultipleFormsDemoView(MultiFormsView):
    template_name = "admin-homepage.html"
    form_classes = {'addofficer': AddOfficerForm,
                    'addpass': MakePassForm,
                    'singledist': SingleDist,
                    'uploadfile' : UploadFileForm,
                    }

    success_urls = {
        'addofficer': 'addedofficer',
        'addpass': 'madepass',
        'singledist': 'distributed',
        'uploadfile' : 'fileuploaded',
    }

    def addofficer_form_valid(self, form):
        netid = form.cleaned_data['target']
        source = form.cleaned_data['source']
        source_user = Student.objects.all().filter(NetId=source)[0]
        target_user = Student.objects.all().filter(NetId=netid)[0]
        if target_user.officer_status is True:
            return HttpResponseRedirect('/admin-homepage/officer-already-added')
        if source_user.officer_status is True:
            source_user.assignOfficer(netid)
        return HttpResponseRedirect('/addedofficer')

    def addpass_form_valid(self, form):
        pass_date = form.cleaned_data['pass_date']
        color = form.cleaned_data['color']
        number = form.cleaned_data['number']
        source = form.cleaned_data['source']
        source_user = Student.objects.all().filter(NetId=source)[0]
        # need to add stuff here
        source_user.officerClubSend(pass_date, number, color)
        return HttpResponseRedirect('/madepass')


    def singledist_form_valid(self, form):
        pk = form.cleaned_data['passes']
        number = form.cleaned_data['number']
        source = form.cleaned_data['source']
        netid = form.cleaned_data['target']
        transferrable = form.cleaned_data['transferrable']
        source_user = Student.objects.all().filter(NetId=source)[0]
        target_pass = Pass.objects.all().filter(pk=pk)[0]
        number = form.cleaned_data['number']
        while number > 0:
            source_user.officerDirectSend(target_pass, netid, transferrable)
            number = number - 1
        return HttpResponseRedirect('/distributed')

    def uploadfile_form_valid(self, form):
        csv_file = form.cleaned_data['file']
        source = form.cleaned_data['source']
        # if not csv_file.name.endswith('.csv'):
        #     messages.error(request,'File is not CSV type')
        #     return HttpResponseRedirect(reverse("myapp:upload_csv"))
        #if file is too large, return
        # if csv_file.multiple_chunks():
        #     messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
        #     return HttpResponseRedirect(reverse("myapp:upload_csv"))

        file_data = csv_file.read().decode("utf-8")     

        lines = file_data.split("\n")
        source_user = Student.objects.all().filter(NetId=source)[0]
        source_user.clear_club()
        i=-1
        for line in lines:       
            if i == -1:
                j = 0
                for entry in line.split(","):
                    if entry.lower().strip() == "netid":
                        i = j
                        break
                    j+=1
            else:
                fields = line.split(",")
                source_user = Student.objects.all().filter(NetId=source)[0]
                source_user.addToClub(fields[i].strip())
        return HttpResponseRedirect('/fileuploaded')

# def add_officer(request):
#     if request.method == 'POST':
#         form = AddOfficerForm(request.POST, prefix='officer')
#         if form.is_valid():
#             netid = form.cleaned_data['target']
#             source = form.cleaned_data['source']
#             source_user = Student.objects.all().filter(NetId=source)[0]
#             if source_user.officer_status is True:
#                 source_user.assignOfficer(netid)
#             return HttpResponseRedirect('/addedofficer')
#     else:
#         form = AddOfficerForm()
#     return render(request, 'admin-homepage.html', {'officerForm': form})

# def add_pass(request):
#     if request.method == 'POST':
#         form = MakePassForm(request.POST, prefix='pass')
#         if form.is_valid():
#             pass_date = form.cleaned_data['pass_date']
#             print(pass_date)
#             color = form.cleaned_data['color']
#             number = form.cleaned_data['number']
#             source = form.cleaned_data['source']
#             source_user = Student.objects.all().filter(NetId=source)[0]
#             # source_user.officerClubSend(pass_date, number, color)
#             return HttpResponseRedirect('/madepass')
#     else:
#         form = MakePassForm()
#     return render(request, 'admin-homepage.html', {'form': form})