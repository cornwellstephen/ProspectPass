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
	name = models.CharField(max_length=60, blank=True)
	user_club = models.CharField(max_length = 200, blank=True)
	officer_status = models.BooleanField(default=False)

	def clear_club(self):
		for student in Student.objects.all().filter(user_club=self.user_club):
			if self.NetId != student.NetId:
				student.user_club = "None"
				student.save()

	def addToClub(self, netid):
		student = Student.objects.all().filter(NetId=netid)[0]
		student.user_club = self.user_club
		student.save()

	@property
	def get_passes(self):
		return self.passes.all().order_by('pass_date', 'club_name')

	def sendpass(self, _pass, user_netid, transferrable):
		user = Student.objects.all().filter(NetId=user_netid)[0]
		_pass.pass_user = user
		_pass.transferrable = transferrable
		_pass.save()

	def activate(self, _pass):
		_pass.activated = True
		_pass.save()

	# def is_officer(user):
	#     return Student.groups.filter(name="Club Officers").exists()

	# creates and distributes the pass to club members
	def officerClubSend(self, p_date, num_passes, color_num):
		if self.officer_status is True:
			for student in Student.objects.all().filter(user_club=self.user_club):
				# one pass for the officer when bulk creating
				if student.officer_status is True:
					_pass = Pass(club_name=self.user_club, pass_date=p_date, pass_user=student,pass_source=student.name,color=color_num,transferrable=True)
					_pass.save()
				else:
					while num_passes > 0:
						_pass = Pass(club_name=self.user_club, pass_date=p_date, pass_user=student,pass_source=student.name,color=color_num,transferrable=True)
						_pass.save()
						num_passes = num_passes - 1
		else:
			pass

	def assignOfficer(self, netid, *args, **kwargs):
		if self.officer_status is True:
			print(Student.objects.all().filter(NetId=netid))
			new_officer = Student.objects.all().filter(NetId=netid)[0]
			new_officer.officer_status = True
			new_officer.save()
		else:
			pass

	def officerDirectSend(self, _pass, user_netid, transferrable):
		if self.officer_status is True:
			if self.user_club == _pass.club_name:
				student = Student.objects.all().filter(NetId=user_netid)[0]
				newpass = Pass(club_name=self.user_club, pass_date=_pass.pass_date, pass_user=student,pass_source=self.name,color=_pass.color,transferrable=transferrable)
				newpass.save()
				self.sendpass(newpass, user_netid, transferrable)
			else:
				self.sendpass(_pass, user_netid, transferrable)
		else:
			pass

	class Meta:
		permissions = (
			("can_create_pass", "To create a pass"),
			("can_distribute_pass", "To distribute passes")
		)

	def __str__(self):
		return self.name

class Pass(models.Model):
	club_name = models.CharField(max_length = 200)
	pass_date = models.DateField()
	pass_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='passes')
	pass_source = models.CharField(max_length = 200, blank=True)
	activated = models.BooleanField(default=False)
	transferrable = models.BooleanField(default=False)
	color = models.IntegerField(blank=True)
	# this is how a pass will be displayed as a string
	def __str__(self):
		return serializers.serialize('json', [self, ])

