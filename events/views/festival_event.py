'''

	Author: Bruce Hansen
	Version: 1.0
	Last Updated: 2/25/2015

	This is the view of events for regular 'Guest' Users.

'''

from django.conf import settings
from base_app.CustomForm import CustomForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import permission_required
import base_app.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.utils import timezone
from django.utils.translation import ugettext as _

templater = get_renderer('events')

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

class EditEventForm(CustomForm):

	''' Class for the form to be used in editing the events. '''

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
	title = "Event Information"
	link = '/events/events'

	name = forms.CharField(required=True, max_length=100)
	start_date = forms.DateField(widget=forms.DateInput)
	end_date = forms.DateField(widget=forms.DateInput)
	venue = forms.ModelChoiceField(queryset=hmod.Venue.objects.all(), empty_label=None)

	## Clean functions ##
	
	# Validate the venue, so that a venue needs to be clicked
	def clean_venue(self):

		empty_venue = hmod.Venue.objects.filter(name='')

		if self.cleaned_data['venue'] == empty_venue[0]:
			raise forms.ValidationError("Please select a venue.")

		return self.cleaned_data['venue']

	# Validate the start and end dates to make sure they're not prior to today's date, and that 
	# the end date doesn't happen before the start date
	def clean(self):

		if self.cleaned_data['start_date'] < timezone.now().date():
			raise forms.ValidationError("The event's start date has already ocurred.")

		if self.cleaned_data['end_date'] < timezone.now().date():
			raise forms.ValidationError("The event's end date has already ocurred.")

		if self.cleaned_data['end_date'] < self.cleaned_data['start_date']:
			raise forms.ValidationError("The event's end date is before the start date.")

		return self.cleaned_data
	

##########################################################################################
################################### DEFAULT ACTION #######################################
##########################################################################################

@view_function
def process_request(request):
	
	# Define the view bag
	params = {}

	# Delete all events that exist in the database with names that are blank
	# (when someone starts an event and abandons it)
	events = hmod.Event.objects.filter(name='').delete()

	# also delete all venues that were created in the creation of the events
	venues = hmod.Venue.objects.filter(name='').delete()

	# Grab all the events from the database
	events = hmod.Event.objects.all().order_by('start_date')
	print(events)

	# Add events to the view bag
	params['events'] = events

	return templater.render_to_response(request, 'festival_event.html', params)

