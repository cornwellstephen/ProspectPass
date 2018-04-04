from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class StudentManager(BaseUserManager):
	def create_user(self, NetId, password=None, **kwargs):

		if not NetId:
			raise ValueError('Users must have a valid NetId.')

		student = self.model(
			NetId=self.normalize_email(NetId)
		)
		
		student.set_password(password)
		student.save()

		return student

	def create_superuser(self, NetId, password=None, **kwargs):
		student = self.create_user(NetId, password, **kwargs)
		student.is_admin = True
		student.save()
		return student

class Student(AbstractBaseUser): # It's now an abstract base user
	username = models.CharField(max_length=40, unique=True) # use the NetId as the username
	NetId = models.CharField(max_length=40, unique=True)
	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
	user_club = models.CharField(max_length = 200)
	password = models.TextField()
	# is_staff = models.BooleanField(
	# 	_('staff status'),
	# 	default=False,
	# 	help_text=_('Designates whether the user can log into this admin site.'),
	# 	)
	is_admin = models.BooleanField(default=False)

	objects = StudentManager()

	USERNAME_FIELD = 'NetId'

	def __str__(self):
		return self.USERNAME_FIELD

	def __unicode__(self):
		return self.NetId

	def get_full_name(self):
		return ' '.join([self.first_name, self.last_name])

	def get_short_name(self):
		return self.first_name


class Pass(models.Model):
	club_name = models.CharField(max_length = 200)
	pass_date = models.DateField()
	club_picture = models.FileField(upload_to='uploads/')
	pass_user = models.ForeignKey(Student, on_delete = models.CASCADE, related_name='passes')
	pass_source = models.CharField(max_length = 200)
	def __str__(self):
		return self.pass_user.user_NetId + ': Passes'