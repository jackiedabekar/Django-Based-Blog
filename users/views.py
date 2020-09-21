from django.shortcuts import render, redirect

#the UserCreationForm is used to create new user aka register
#new user, thats why we are using UserCreationForm
from django.contrib.auth.forms import UserCreationForm

#this is used to send messages to user 
from django.contrib import messages

from .forms import UserRegisterForm, UserUpdateForm, UserProfileUpdateForm

#this below decorator is used to verify if user is login or not
#when he/she want check other post or data, for
#example you cant send msg or view some1 profile unless you are login
from django.contrib.auth.decorators import login_required

def register(request):
	"""
	This View Is Used To Create New User By 
	Using Inbuilt Djnago UserCreationForm, from django.contrib.auth.forms
	"""
	#Check if request method type is post or get
	#Post request is done when user want to alter the state of DB
	if request.method == 'POST':
		#pass the request to UserCreationForm
		form = UserRegisterForm(request.POST)
		#check if data is valid or not
		#the .is_valid() check for all the validation
		#check like password matching, same username in DB, etc
		#if form is valid the .is_valid() funtion become true and then
		# convert the request.post to dictionary by name cleaned_data
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			# display the message for user for form submition
			# bu using messages for django.contrib import messages
			messages.success(request, f'{username} Your account has been created!')
			# when request is valid and data is clean make suer to redirect to another page
			# or else user will resubmit the from by thinking form is not submit
			return redirect('login')
	else:
		# if form data is not valid
		form = UserRegisterForm()
	return render(request,'users/register.html', {'title': 'Registration','form' : form})



@login_required
def profile(request):
	"""
	This view handels the profile of user and check if user is 
	login or not to make him/her to access his/her profile or others data 
	only if he/she is login with login_required decorator 
	"""
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = UserProfileUpdateForm(request.POST,
										request.FILES, 
										instance= request.user.userprofile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your Account Has Updated')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = UserProfileUpdateForm(instance= request.user.userprofile) 
	context = {
		'u_form' : u_form,
		'p_form' : p_form
	}
	return render(request, 'users/profile.html', context)

