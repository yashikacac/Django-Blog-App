from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	# user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default =1)
	# user1 = models.ForeignKey(User, on_delete=models.CASCADE, unique = True, default =1)
	p_image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'
