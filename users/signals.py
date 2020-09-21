'''
Here we have created a signal, that when a New User get created
create a signal that tell the UserPrfile model(which handel Profile Pic creation) 
to create and save profile pic realated to that patricular
user
'''

#the below line one of the signal django provide us
#post_save is use to create user profile
from django.db.models.signals import post_save

#here User will act as sender, thats why User is Imported
from django.contrib.auth.models import User

#the receiver is a decorator who act as a receiver
#and take 2 input 1)what is the signal 2)who is the sender
from django.dispatch import receiver

#the User Profile will be the receiver here
#wgo gonna recevie signal from User fot createing profile
#for new created user
from .models import UserProfile

#the receiver decorator is which provide 
#extra functionality to function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	"""
	This function is used to create profile for new user
	which takes 4 input:- the sender, which is provider by recever decorator,
	instance:- current user
	created:- what to do if created is True 
	and **kwargs
	"""
	#when new user is created
	if created:
		#do this
		UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_post(sender, instance, **kwargs):
	"""
	Ths save_post function is used to save the post
	which is created by the create_profile function
	"""
	instance.userprofile.save()