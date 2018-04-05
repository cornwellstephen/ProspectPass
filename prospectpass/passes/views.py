from django.shortcuts import render

from rest_framework import permissions, viewsets

from passes.models import Student
from passes.permissions import IsStudentOwner
from passes.serializers import StudentSerializer

from django.views import generic
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
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
	lookup_field = 'NetId'
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		if self.request.method == 'POST':
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsStudentOwner(),)

	def create(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			Student.objects.create_user(**serializer.validated_data)
			return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
		return Response({
			'status': 'Bad request',
			'message': 'Student could not be created with received data.'
		}, status=status.HTTP_400_BAD_REQUEST)
