'''

	Author: John Turner
	Version: 2.0
	Last Updated: 3/17/2015

	View for all CRUD functions for the groups.

'''

from django.conf import settings
from base_app.CustomForm import CustomForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import base_app.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth import authenticate, login, logout
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import send_mail
from django.core.mail import EmailMessage


templater = get_renderer('homepage')

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

class LoginForm(CustomForm):

	''' Class for the login form '''
	
	username = forms.CharField(required=True, max_length=100)
	password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput)

	def clean(self):

		# Check to see if self is valid
		#if self.is_valid():




			#log user in

			# See if username and password combo is correct
			#user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])

			#if user is None:
			#	raise forms.ValidationError("Incorrect Username and/or Password")

		return self.cleaned_data

##########################################################################################
############################### RESET PASSWORD - EMAIL CLASS #############################
##########################################################################################

class EmailForm(CustomForm):

	''' Class for the form where users submit their email to get a password reset link '''
	
	# No delete button or cancel button
	delete_button = False
	cancel_button = False

	title = ''

	email = forms.CharField(required=True, max_length=100)

	def clean(self):

		# Check to see if self is valid
		if self.is_valid():

			# See if the email exists in the database
			try:
				user = hmod.User.objects.get(email=self.cleaned_data['email'])
			except hmod.User.DoesNotExist:
				raise forms.ValidationError('This email does not exist in our system!')

		return self.cleaned_data

##########################################################################################
################################## LOGIN USER ACTION #####################################
##########################################################################################

@view_function
def process_request(request):
	
	# Define the view bag
	params={}

	form = LoginForm(request)

	# If the user was brought here from the front-page login button, return the ajax form
	# If not, send user to the main login page. 
	if request.urlparams[0] == 'modal':
		form.modal = True
	else:
		form.modal = False

	## IF POST METHOD OCCURRED ##
	if request.method == 'POST':

		form = LoginForm(request, request.POST)

		if request.urlparams[0] == 'modal':
			form.modal = True
		else:
			form.modal = False

		if form.is_valid():

			#
			 validate against active directory
			#s = Server('byuldap.byu.edu', port=389, get_info=GET_ALL_INFO)
			#c = Connection(s, auto_bind = true, client_strategy = STRATEGY_SYNC,
			#user='cn=pearl18,ou=people,o-ces', password='idahorocks18', authentication=AUTH_SIMPLE)

			#if c is not None :
				#u = amod.User.objects.get_or_create(username=form.cleaned_data['username'])
				#u.first_name = 
				#u.last_name = 
				#u.email
				#u.set_password()
				#u.save()

			## Authenticate again
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			
			login(request, user)

			## REDIRECT TO PAGE IF USER WAS ON THEIR WAY SOMEWHERE ##
			if request.GET.get('next') is not None:
				return HttpResponseRedirect(request.GET.get('next'))
			else:
				## OTHERWISE REDIRECT TO ACCOUNT PAGE ##
				return HttpResponse('''
					<script>
						window.location.reload()
					</script>
				''')

	params['form'] = form



	# If the user was brought here from the front-page login button, return the ajax form
	# If not, send user to the main login page. 
	if form.modal:
		return templater.render_to_response(request, 'modal_login.html', params)
	else:
		return templater.render_to_response(request, 'login.html', params)

##########################################################################################
################################## RESET PASSWORD ACTION #################################
##########################################################################################

@view_function
def reset_password(request):

	'''
		Takes the user to the reset password page, where they enter their email. 
		Once entered, an email is sent to the user with a link through which they 
		can reset their password.
	'''

	# Define the view bag
	params={}

	form = EmailForm(request)

	if request.method == "POST":

		form = EmailForm(request, request.POST)

		if form.is_valid():
			
			email = form.cleaned_data['email']
			
			## Email the user here!!
			subject="Email, Password Reset"

			body = templater.render(request, 'forgot_password.html', params)  

			send_mail(subject, body, 'brucehnsn@gmail.com', [email], html_message=body, fail_silently = False)



			## Send user to the "email sent" page
			return templater.render_to_response(request, 'email_sent.html', params)

	params['form'] = form

	return templater.render_to_response(request, 'password_reset_email.html', params)

##########################################################################################
################################## LOGOUT USER ACTION ####################################
##########################################################################################

@view_function

def logout_user(request):
	
	logout(request)

	return HttpResponseRedirect('/homepage/index/')