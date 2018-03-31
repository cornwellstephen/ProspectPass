from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser): # It's now an abstract base user
	user_netid = models.CharField(max_length = 200)
	username = models.CharField(max_length=40, unique=True)
	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
	user_club = models.CharField(max_length = 200)
	password = models.TextField()
	is_admin = models.BooleanField(default=False)
	def __str__(self):
			return self.user_name

class Pass(models.Model):
	club_name = models.CharField(max_length = 200)
	pass_date = models.DateField()
	club_picture = models.FileField(upload_to='uploads/')
	pass_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='passes')
	pass_source = models.CharField(max_length = 200)
	def __str__(self):
		return self.pass_user.user_netid + ': Passes'