'''

	Author: John Turner
	Version: 1.0
	Last Updated: 3/6/2015

	View for the functions related to the Shopping Cart

'''

from django.conf import settings
from base_app.CustomForm import CustomForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import login_required, permission_required
import base_app.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.utils.translation import ugettext as _
from base_app.CustomWidgets import CustomSelect, CustomRadioRenderer
from django.contrib.auth import authenticate, login, logout
import requests
from datetime import datetime, timedelta
import datetime
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import send_mail
from django.core.mail import EmailMessage


templater = get_renderer('account')

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

class ShippingForm(CustomForm):

	''' Class for the form to be used adding shipping info. '''

	# List of constants for the states:
	ALASKA = 'AK'
	ALABAMA = 'AL'
	ARKANSAS = 'AR'
	ARIZON = 'AZ'
	CALIFORNIA = 'CA'
	COLORADO = 'CO'
	CONNECTICUT = 'CT'
	DELAWARE = 'DE'
	FLORIDA = 'FL'
	GEORGIA = 'GA'
	HAWAII = 'HI'
	IOWA = 'IA'
	IDAHO = 'ID'
	ILLINOIS = 'IL'
	INDIANA = 'IN'
	KANSAS = 'KS'
	LOUISIANA = 'LA'
	MASSACHUSETTS = 'MA'
	MARYLAND = 'MD'
	MAINE = 'ME'
	MICHIGAN = 'MI'
	MINNESOTA = 'MN'
	MISSOURI = 'MO'
	MISSISSIPPI = 'MS'
	MONTANA = 'MT'
	NORTH_CAROLINA = 'NC'
	NORTH_DAKOTA = 'ND'
	NEBRASKA = 'NE'
	NEW_HAMPSHIRE = 'NH'
	NEW_JERSEY = 'NJ'
	NEW_MEXICO = 'NM'
	NEVADA = 'NV'
	NEW_YORK = 'NY'
	OHIO = 'OH'
	OKLAHOMA = 'OK'
	OREGON = 'OR'
	PENNSYLVANIA = 'PA'
	RHODE_ISLAND = 'RI'
	SOUTH_CAROLINA = 'SC'
	SOUTH_DAKOTA = 'SD'
	TENNESSEE = 'TN'
	TEXAS = 'TX'
	UTAH = 'UT'
	VIRGINIA = 'VA'
	VERMONT = 'VT'
	WASHINGTON = 'WA'
	WISCONSIN = 'WI'
	WEST_VIRGINIA = 'WV'
	WYOMING = 'WY'

	# Choices list of tuples for the car_states field
	STATE_CHOICES = (
		(ALASKA, 'Alaska'),
		(ALABAMA, 'Alabama'),
		(ARKANSAS, 'Arkansas'),
		(ARIZON, 'Arizon'),
		(CALIFORNIA, 'California'),
		(COLORADO, 'Colorado'),
		(CONNECTICUT, 'Connecticut'),
		(DELAWARE, 'Delaware'),
		(FLORIDA, 'Florida'),
		(GEORGIA, 'Georgia'),
		(HAWAII, 'Hawaii'),
		(IOWA, 'Iowa'),
		(IDAHO, 'Idaho'),
		(ILLINOIS, 'Illinois'),
		(INDIANA, 'Indiana'),
		(KANSAS, 'Kansas'),
		(LOUISIANA, 'Louisiana'),
		(MASSACHUSETTS, 'Massachusetts'),
		(MARYLAND, 'Maryland'),
		(MAINE, 'Maine'),
		(MICHIGAN, 'Michigan'),
		(MINNESOTA, 'Minnesota'),
		(MISSOURI, 'Missouri'),
		(MISSISSIPPI, 'Mississippi'),
		(MONTANA, 'Montana'),
		(NORTH_CAROLINA, 'North Carolina'),
		(NORTH_DAKOTA, 'North Dakota'),
		(NEBRASKA, 'Nebraska'),
		(NEW_HAMPSHIRE, 'New Hampshire'),
		(NEW_JERSEY, 'New Jersey'),
		(NEW_MEXICO, 'New Mexico'),
		(NEVADA, 'Nevada'),
		(NEW_YORK, 'New York'),
		(OHIO, 'Ohio'),
		(OKLAHOMA, 'Oklahoma'),
		(OREGON, 'Oregon'),
		(PENNSYLVANIA, 'Pennsylvania'),
		(RHODE_ISLAND, 'Rhode Island'),
		(SOUTH_CAROLINA, 'South Carolina'),
		(SOUTH_DAKOTA, 'South Dakota'),
		(TENNESSEE, 'Tennessee'),
		(TEXAS, 'Texas'),
		(UTAH, 'Utah'),
		(VIRGINIA, 'Virginia'),
		(VERMONT, 'Vermont'),
		(WASHINGTON, 'Washington'),
		(WISCONSIN, 'Wisconsin'),
		(WEST_VIRGINIA, 'West Virginia'),
		(WYOMING, 'Wyoming'),
	)

	## Class title ##
	title = "Shipping Information"
	link = "products/products"

	# Don't include the delete button.
	delete_button = False

	# Submit text
	submit_text = 'Continue'

	## Form Inputs ##
	address1 = forms.CharField(required=True, max_length=100)
	address2 = forms.CharField(required=False, max_length=100)
	city = forms.CharField(required=True, max_length=100)
	state = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=CustomSelect)
	ZIP = forms.CharField(required=True)

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

class PaymentForm(CustomForm):

	''' Class for the form for payment info. '''

	## Class title ##
	title = "Payment Info"
	link = "products/products"

	# Don't include the delete button.
	delete_button = False

	# Submit text
	submit_text = 'Continue'

	## Form Inputs ##
	name = forms.CharField(required=True, max_length=100)
	credit_card_number = forms.CharField(required=True, max_length=100)
	security_code = forms.IntegerField(required=True)
	exp_month = forms.CharField(required=True, max_length=2)
	exp_year = forms.CharField(required=True, max_length=4)
	card_company = forms.CharField(max_length=100)

	def clean(self):

		API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
		API_KEY = 'cd0bea8de66c6bdd2ba2a87301a705d9'

		r= requests.post(API_URL, data = {
			 'apiKey': API_KEY, 
			 'currency': 'usd', 
			 'amount': self.request.session['total'],
			 'type': self.cleaned_data['card_company'],
			 'number': self.cleaned_data['credit_card_number'],
			 'exp_month': self.cleaned_data['exp_month'], 
			 'exp_year': self.cleaned_data['exp_year'], 
			 'cvc': self.cleaned_data['security_code'], 
			 'name': self.cleaned_data['name'], 
			 'description': 'Charge for cosmo@is411.byu.edu',
		})

		print(r.text)

		# parse response to a dictionary
		resp = r.json()
		if 'error' in resp: # error?
			raise forms.ValidationError("ERROR: " + resp['error'])

		else:
			print(resp.keys())
			print(resp['ID'])

		return self.cleaned_data
##########################################################################################
################################# DEFAULT ACTION #########################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):
	
	# Define the view bag
	params = {}

	# Create a shopping cart in the session if it doesn't already exist
	if 'cart' not in request.session:
		request.session['cart'] = {}

	# Make sure the session variable recognizes the change
	request.session.modified = True

	# Dictionary for items
	items = {}

	# Grab the items from the shopping cart:
	for pid in request.session['cart']:

		try:
			item = hmod.Inventory.objects.get(id=pid)
		except hmod.Inventory.DoesNotExist:
			return HttpResponse('failed getting item')

		items[item] = request.session['cart'][pid]

	params['items'] = items
	params['total'] = 0

	return templater.render_to_response(request, 'ShoppingCart.html', params)

##########################################################################################
################################### ADD ITEM ACTION ######################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def add(request):
	
	# Define the view bag
	params = {}

	# Create the shopping cart if it already hasn't been
	if 'cart' not in request.session:
		request.session['cart'] = {}

	# Grab the item according to the data passed in the GET
	pid = request.REQUEST.get('id')
	quantity = int(request.REQUEST.get('quantity'))

	if pid in request.session['cart']:
		request.session['cart'][pid] += quantity
	else:
		request.session['cart'][pid] = quantity

	# Make sure the session variable recognizes the change
	request.session.modified = True



	return HttpResponseRedirect('/account/ShoppingCart/')

##########################################################################################
################################ REMOVE ITEM ACTION ######################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def remove(request):
	''' 
		Removes an item from the shopping cart. 
	'''

	# Define the view bag
	params = {}

	# Grab the item id
	pid = request.REQUEST.get('id')

	# Remove from the shopping cart
	if pid in request.session['cart']:

		del request.session['cart'][pid]

	request.session.modified = True

	return HttpResponseRedirect('/account/ShoppingCart/')

##########################################################################################
################################# CHECKOUT FUNCTION ######################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def checkout(request):
	'''
		Sends the user to the shipping info page.
	'''

	# Define the view bag
	params={}

	# Grab the user
	try:
		user = hmod.User.objects.get(id=request.user.id)
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/products/products/')

	# Pass in user data to the form
	form = ShippingForm(request, initial={
		'address1': user.address.address1,
		'address2': user.address.address2,
		'city': user.address.city,
		'state': user.address.state,
		'ZIP': user.address.ZIP,
		})

	if request.method == 'POST':

		# Validate the form
		form = ShippingForm(request, request.POST)

		if form.is_valid():

			# Return user to list
			return HttpResponseRedirect('/account/ShoppingCart.payment/')

	params['form'] = form

	return templater.render_to_response(request, 'ShippingInfo.html', params)

##########################################################################################
################################ CREDIT CARD INFO FUNCTION ###############################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def payment(request):
	'''
		Sends the user to the payment page.
	'''

	# Define the view bag
	params={}

	# Pass in user data to the form
	form = PaymentForm(request)

	if request.method == 'POST':

		# Validate the form
		form = PaymentForm(request, request.POST)

		if form.is_valid():

			# Return user to list
			return HttpResponseRedirect('/account/ShoppingCart.confirmation/')

	params['form'] = form

	return templater.render_to_response(request, 'PaymentInfo.html', params)

##########################################################################################
################################### CONFIRMATION ACTION ##################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def confirmation(request):
	'''
		Sends the user to the confirmation page.
	'''

	# Define the view bag
	params={}

	### update the rental period if a rental ###
	#create dictionary for items
	inventory = {}

	# create a transaction

	transaction = hmod.Transaction()
	transaction.customer = request.user
	transaction.transaction_date = datetime.datetime.now()
	transaction.save()

	# Grab the items from the shopping cart:
	for pid in request.session['cart']:

		try:
			inv=hmod.Item.objects.get(id=pid)
			rentable = True
		except hmod.Item.DoesNotExist:
			try: 
				inv=hmod.Inventory.objects.get(id=pid)
				rentable=False
			except:
				return HttpResponse('Item does not exist')

		if not rentable:
			inv.quantity_on_hand -= request.session['cart'][pid]

			si = hmod.SaleItem()
			si.product = inv
			print(si.product)
			si.quantity = request.session['cart'][pid]
			si.amount = inv.specs.price * request.session['cart'][pid]
			si.transaction = transaction

			si.save()

		else:
			inv.quantity_on_hand -= 1
			inv.owner = transaction.customer
			inv.times_rented += 1

			#make rental line item
			ri = hmod.RentalItem()
			ri.date_out = datetime.date.today()
			ri.due_date = datetime.date.today() + timedelta(days=request.session['cart'][pid])
			ri.amount = inv.standard_rental_price * request.session['cart'][pid]
			ri.item = inv
			ri.transaction = transaction

			ri.save()

			inv.save()

	email = request.user.email
	

	### view current rentals
	# get the transactions for the active user, this is to populate the rentals that the user has
	transaction = hmod.Transaction.objects.filter(customer_id=request.user.id)

	for tran in transaction:
		# Grab the items without a date_in and where the customer is the current user
		r_items = hmod.RentalItem.objects.filter(transaction_id=tran.id).filter(date_in=None)

		params['r_items'] = r_items
	### end view current rentals





	for li in transaction.saleitem_set.all():
		print(li)



	items = []
	quantity = []

	for item_id in request.session['cart']:
		try:
			items.append(hmod.Inventory.objects.get(id=item_id))
		except:
			HttpResponse('Item does not exist')

		item.quantity = request.session['cart'][item_id]

	params['items'] = items

	subject="Receipt for Colonial Heritage Foundation"

	body = templater.render(request, 'rentalscheckout_sendemail.html', params)  

	send_mail(subject, body, 'brucehnsn@gmail.com', [request.user.email], html_message=body, fail_silently = False)

	request.session['cart'] = {}

	return templater.render_to_response(request, 'confirmation.html', params)

##########################################################################################
################################### CONFIRMATION ACTION ##################################
##########################################################################################

