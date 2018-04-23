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
from .forms import PassForm, AddOfficerForm
from django.http import HttpResponseRedirect
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
	# lookup_field = 'NetId'
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

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

def send_pass(request, pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PassForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            netid = form.cleaned_data['target']
            source = form.cleaned_data['source']
            # passId = form.cleaned_data['passId']
            source_user = Student.objects.all().filter(NetId=source)[0]
            target_pass = Pass.objects.all().filter(pk=pk)[0]
            if source_user.officer_status is True:
                source_user.officerDirectSend(target_pass, netid)
            else:
                source_user.sendpass(target_pass, netid)
            return HttpResponseRedirect('/sentpass')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PassForm()

    return render(request, 'sendpass.html', {'form': form})

def add_officer(request):
    if request.method == 'POST':
        form = AddOfficerForm(request.POST)
        if form.is_valid():
            netid = form.cleaned_data['target']
            source = form.cleaned_data['source']
            source_user = Student.objects.all().filter(NetId=source)[0]
            new_officer = Student.objects.all().filter(NetId=netid)[0]
            if source_user.officer_status is True:
                source_user.assignOfficer(new_officer)
            return HttpResponseRedirect('/addedofficer')
    else:
        form = AddOfficerForm()
    return render(request, 'addofficer.html', {'form': form})