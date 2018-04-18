from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission
from django.core import serializers



class Student(AbstractUser): # It's now an abstract base user
	# username = models.CharField(max_length=40, blank=True) # use the NetId as the username
	NetId = models.CharField(max_length=40, blank=True)
	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
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

	def __str__(self):
		return self.first_name + " " + self.last_name

class Pass(models.Model):
	club_name = models.CharField(max_length = 200)
	pass_date = models.DateField()
	club_picture = models.FileField(upload_to='uploads/', blank=True)
	pass_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='passes')
	pass_source = models.CharField(max_length = 200, blank=True)
	activated = models.BooleanField(default=False)
	transferable = models.BooleanField(default=False)
	color = models.CharField(max_length=200, blank=True)
	# this is how a pass will be displayed as a string
	def __str__(self):
		return serializers.serialize('json', [self, ])

