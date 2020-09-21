from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='user.png', upload_to='profile_pic')

	def __str__(self):
		return f'{self.user.username} Profile'

	#overwritten save method to reduce size of image and
	# save it again
	def save(self, **kwargs):
		super().save()
		img = Image.open(self.image.path) 
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)