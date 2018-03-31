from django.db import models

# Create your models here.
class User(models.Model): # Have to fix this section to be a proper Django user
	user_netid = models.CharField(max_length = 200)
	user_name = models.CharField(max_length = 200)
	user_club = models.CharField(max_length = 200)
	password = models.TextField()
	is_staff = models.BooleanField()


class Pass(models.Model):
	club_name = models.CharField(max_length = 200)
	pass_date = models.DateField()
	club_picture = models.FileField(upload_to='uploads/')
	pass_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='passes')
	pass_source = models.CharField(max_length = 200)
	def __str__(self):
		return self.pass_user.user_netid + ': Passes'