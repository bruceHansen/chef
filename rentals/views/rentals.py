'''

	Author: John Turner
	Version: 1.0
	Last Updated: 3/20/2015

	View that manages the client-facing products section of the website. 

'''

from django.conf import settings
from base_app.CustomForm import CustomForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import login_required, permission_required
import base_app.models as hmod
from django.utils.translation import ugettext as _
from django_mako_plus.controller.router import get_renderer
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from decimal import *
import datetime

templater = get_renderer('rentals')

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

# Non-Wardrobe form class
class EditNWItemForm(CustomForm):

	''' Class for the form to be used in editing the non-wardrobe items. '''

	## Class title ##
	title = "Item Information"

	## Link ##
	link = '/inventory/items'

	## Special Delete Type ##
	delete_type = '_nw'

	name = forms.CharField(required=True, max_length=100)
	description = forms.CharField(widget=forms.Textarea(attrs={'rows' : 3}), max_length=250)
	value = forms.DecimalField(max_digits=10, decimal_places=2)
	is_rentable = forms.BooleanField(required=False)
	standard_rental_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2)
	owner = forms.ModelChoiceField(queryset=hmod.User.objects.all(), empty_label=None)

	## Clean functions ##
	
	# If is_rentable is checked, standard_rental_price better have something in it
	def clean_standard_rental_price(self):

		if self.cleaned_data['is_rentable'] is True and self.cleaned_data['standard_rental_price'] == 0:
			raise forms.ValidationError(_("Please add a rental price."))

		return self.cleaned_data['standard_rental_price']

	# Make sure an owner is selected
	def clean_owner(self):

		empty_owner = hmod.User.objects.filter(username='')

		if self.cleaned_data['owner'] == empty_owner[0]:
			raise forms.ValidationError("Please select an owner.")

		return self.cleaned_data['owner']
	

# Wardrobe Item Form, extends previous
class EditWItemForm(EditNWItemForm):

	## Special Delete Type ##
	delete_type = '_w'

	''' Class for the form to be used in editing wardrobe items '''

	size = forms.IntegerField()
	size_modifier = forms.CharField(max_length=100, required=False)
	gender = forms.CharField(max_length=1)
	color = forms.CharField(max_length=100)
	pattern = forms.CharField(max_length=100)
	start_year = forms.DateField()
	end_year = forms.DateField()
	note = forms.CharField(required=False, max_length=255, widget=forms.Textarea(attrs={ 'rows' : 4 }))

    ## Clean functions ##
    
    # Make sure the years are correct (start year is before end year)

class DamageForm(CustomForm):

    ''' Class for the login form '''

    username = forms.CharField(required=True, max_length=100)
    password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput)
    damages = forms.CharField(required=False, label="Damage Description", max_length=2000)
    damage_fee = forms.DecimalField(required=False, decimal_places=2, label="Damage Fees", max_value=1000000.00)

    def clean(self):

        # Check to see if self is valid
        if self.is_valid():

            if self.cleaned_data['damage_fee'] is None:
                self.cleaned_data['damage_fee'] = Decimal('0')

            # See if username and password is correct
            user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])

            if user is None:
                raise forms.ValidationError("Incorrect Username and/or Password")
            else:
                try:
                    agents = hmod.User.objects.get(username=self.cleaned_data['username'])
                except hmod.User.DoesNotExist:
                    return HttpResponseRedirect('/rentals/rentals.returns/')

                if not agents.groups.filter(name='Administrator').exists():
                    raise forms.ValidationError("Please have a manager approve your return")

        return self.cleaned_data


##########################################################################################
###################################### DEFAULT ACTION ####################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):
	
	# Define the view bag
	params = {}

	# Delete all items that exist in the database with names that are blank
	# (when someone starts an item and abandons it)
	rentals = hmod.Inventory.objects.filter(shelf_location='').delete()
	items   = hmod.Item.objects.filter(shelf_location='').delete()
	items   = hmod.WardrobeItem.objects.filter(shelf_location='').delete()

	# Grab all the items and wardrobe items from the database that are available for rent
	items = hmod.Item.objects.all().filter(wardrobeitem=None).exclude(standard_rental_price=None).exclude(times_rented=None).exclude(price_per_day=None).order_by('specs__name')

	params['non_wardrobe'] = items

	items = hmod.WardrobeItem.objects.all().exclude(standard_rental_price=None).exclude(times_rented=None).exclude(price_per_day=None).order_by('specs__name')

	params['wardrobe'] = items

	return templater.render_to_response(request, 'rentals.html', params)

##########################################################################################
######################################## ITEM DETAILS ####################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def details(request):
	
	# Define the view bag
	params={}

	try:
		item = hmod.Item.objects.get(id=request.urlparams[0])
	except hmod.Item.DoesNotExist:
		return HttpResponseRedirect('/rentals/rentals/')

	params['item'] = item

	return templater.render_to_response(request, 'ItemDetails.html', params)


##########################################################################################
################################## Display Rental ITEMS ###################################
##########################################################################################

@view_function
@permission_required('base_app.add_item', login_url='/homepage/login/')
def rental_return(request):
	
	# Define the view bag
	params={}

	# get the transactions for the active user
	rental_items = []

	r_items = hmod.RentalItem.objects.all().filter(date_in=None)
	print(r_items)

	for r_item in r_items:
		if r_item.transaction.customer == request.user:
			rental_items.append(r_item)
			print(rental_items)

	params['rented_items'] = rental_items

	return templater.render_to_response(request, 'rental_return.html', params)


##########################################################################################
################################## RETURN Specific ITEMS ###################################
##########################################################################################


@view_function
def item_return(request):

    # Define the view bag
    params={}
    form = DamageForm(request)
    form.cancel_button = False
    form.delete_button = False
    form.submit_text = "Complete Return"

    try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
    except hmod.Item.DoesNotExist:
        return HttpResponseRedirect('/rentals/rentals.returns/')

    try:
        l_item = hmod.RentalItem.objects.get(id=request.urlparams[1])
    except hmod.RentalItem.DoesNotExist:
        return HttpResponseRedirect('/rentals/rentals.returns/')

    date = hmod.RentalItem.objects.filter(due_date__range=[datetime.datetime.now(), '3000-01-01']).filter(item=item).order_by('due_date')

    if request.method == 'POST':
        form = DamageForm(request, request.POST)
        form.cancel_button = False
        form.delete_button = False
        form.submit_text = "Complete Return"

        if form.is_valid():
            ## Authenticate again
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            ## COMPLETE RETURN ##
            l_item.date_in = datetime.date.today()
            l_item.agent = user

            item.quantity_on_hand +=1

            #create damage fee line item 
            if len(form.cleaned_data['damages']) > 1 or Decimal(form.cleaned_data['damage_fee']) > 0:
                d_fee = hmod.DamageFee()
                d_fee.amount = Decimal(form.cleaned_data['damage_fee'])
                d_fee.description = form.cleaned_data['damages']
                d_fee.transaction = l_item.transaction
                d_fee.save()

            l_item.save()
            item.save()

            return templater.render_to_response(request, 'items_returned.html', params)

    params['form'] = form
    params['lineItem'] = l_item
    params['item'] = item
    params['date'] = date

    return templater.render_to_response(request, 'return_item.html', params)

##########################################################################################
##################################### SEARCH FORM ACTION #################################
##########################################################################################

# @view_function
# def search(request):

# 	# Define the view bag
# 	params = {}

# 	# If a name has been passed in, then search for the item and return the details page
# 	if request.REQUEST.get('name') is not None:

# 		try:
# 			product = hmod.Inventory.objects.get(specs__name=request.REQUEST.get('name'),item=None)

# 			return HttpResponse('/products/products.details/{0}'.format(product.id))

# 		except hmod.Inventory.DoesNotExist:

# 			return HttpResponse('Product not found')

# 	return templater.render_to_response(request, 'Search.html', params)