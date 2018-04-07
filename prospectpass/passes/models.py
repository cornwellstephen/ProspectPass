from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings

# Create your models here.
# class StudentManager(BaseUserManager):
# 	def create_user(self, NetId, password=None, **kwargs):

# 		if not NetId:
# 			raise ValueError('Users must have a valid NetId.')

# 		student = self.model(
# 			NetId=self.normalize_email(NetId)
# 		)
		
# 		student.set_password(password)
# 		student.save()

# 		return student

# 	def create_superuser(self, NetId, password=None, **kwargs):
# 		student = self.create_user(NetId, password, **kwargs)
# 		student.is_superuser = True
# 		student.is_staff = True
# 		student.save()
# 		return student

class Student(AbstractUser): # It's now an abstract base user
	# username = models.CharField(max_length=40, blank=True) # use the NetId as the username
	NetId = models.CharField(max_length=40, blank=True)
	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
	user_club = models.CharField(max_length = 200)

	def get_passes(self):
		return self.passes.all()

	def sendpass(self, _pass, user_netid):
		user = Student.objects.all().filter(NetId=user_netid)[0]
		_pass.pass_user = user
		_pass.save()

	# def __str__(self):
	# 	return self.first_name + " " + self.last_name



class Pass(models.Model):
	club_name = models.CharField(max_length = 200)
	pass_date = models.DateField()
	club_picture = models.FileField(upload_to='uploads/')
	pass_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='passes')
	pass_source = models.CharField(max_length = 200)
	def __str__(self):
		return self.pass_user.NetId + ': ' + self.club_name + ' | ' + str(self.pass_date)