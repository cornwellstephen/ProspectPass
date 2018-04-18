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
from .forms import PassForm
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

class StudentViewSet(viewsets.ModelViewSet):
	# lookup_field = 'NetId'
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class PassViewSet(viewsets.ModelViewSet):
	queryset = Pass.objects.all()
	serializer_class = PassSerializer

def send_pass(request):
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
            target_user = Student.objects.all().filter(NetId=netid)
            source_user = Student.objects.all().filter(NetId=source)
            
            # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PassForm()

    return render(request, 'sendpass.html', {'form': form})
