from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings

<<<<<<< Updated upstream
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission

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
=======
>>>>>>> Stashed changes

class Student(AbstractUser): # It's now an abstract base user
	# username = models.CharField(max_length=40, blank=True) # use the NetId as the username
	NetId = models.CharField(max_length=40, blank=True)
	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
<<<<<<< Updated upstream
	user_club = models.CharField(max_length = 200, blank=True)
	officer_status = models.BooleanField(default=False)

	def get_passes(self):
		return self.passes.all()

	def sendpass(self, _pass, user_netid):
		user = Student.objects.all().filter(NetId=user_netid)[0]
		_pass.pass_user = user
		_pass.save()

	def activate(self, _pass):
		_pass.activated = True
		_pass.save()

	# def is_officer(user):
	#     return Student.groups.filter(name="Club Officers").exists()

	# creates and distributes the pass to club members
	def officerClubSend(self, p_date, num_passes):
		if self.officer_status is True:
			for student in Student.objects.all().filter(user_club=self.user_club):
				# one pass for the officer when bulk creating
				if student.officer_status is True:
					_pass = Pass(club_name=self.user_club, pass_date=p_date, pass_user=student,pass_source=student.first_name + ' ' + student.last_name)
					_pass.save()
				else:
					while num_passes > 0:
						_pass = Pass(club_name=self.user_club, pass_date=p_date, pass_user=student,pass_source=student.first_name + ' ' + student.last_name)
						_pass.save()
						num_passes = num_passes - 1
		else:
			pass

	def assignOfficer(person):
		if self.officer_status is True:
			person.officer_status = True
			person.save()
		else:
			pass

	def officerDirectSend(self, _pass, user_netid):
		if self.officer_status is True:
			student = Student.objects.all().filter(NetId=user_netid)[0]
			newpass = Pass(club_name=self.user_club, pass_date=_pass.pass_date, pass_user=student,pass_source=self.first_name + ' ' + self.last_name)
			newpass.save()
			self.sendpass(newpass, user_netid)
		else:
			pass

	class Meta:
		permissions = (
			("can_create_pass", "To create a pass"),
			("can_distribute_pass", "To distribute passes")
		)

	# def __str__(self):
	# 	return self.first_name + " " + self.last_name

=======
	user_club = models.CharField(max_length = 200)
>>>>>>> Stashed changes


class Pass(models.Model):
	club_name = models.CharField(max_length = 200)
	pass_date = models.DateField()
	club_picture = models.FileField(upload_to='uploads/')
	pass_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='passes')
	pass_source = models.CharField(max_length = 200, blank=True)
	activated = models.BooleanField(default=False)
	transferrable = models.BooleanField(default=False)
	# this is how a pass will be displayed as a string
	def __str__(self):
		return self.pass_user.NetId + ': ' + self.club_name + ' | ' + str(self.pass_date)