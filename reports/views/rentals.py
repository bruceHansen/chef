'''

    Author: John Turner
    Version: 1.0
    Last Updated: 3/6/2015

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
import datetime
from django.core.mail import send_mail

templater = get_renderer('reports')

##########################################################################################
###################################### DEFAULT ACTION ####################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):

    # Define the view bag
    params = {}

    return templater.render_to_response(request, 'products.html', params)

##########################################################################################
################################## OVERDUE RENTALS REPORT ################################
##########################################################################################

@view_function
@permission_required('base_app.add_item', login_url='/homepage/login/')
def overdue(request):

    # Define the view bag
    params={}

    #define now
    now = datetime.datetime.now()

    #Create variables for the days overdue
    thirty = now - datetime.timedelta(days=30)
    sixty = now - datetime.timedelta(days=60)
    ninety = now - datetime.timedelta(days=90)

    #grab items that are less than thirty days overdue(1-29)
    thirty_days = hmod.RentalItem.objects.filter(due_date__range=[thirty, now], date_in=None)
    params['thirty'] = thirty_days

    #Grab the items that are thirty to sixty days overdue(30-59)
    sixty_days = hmod.RentalItem.objects.filter(due_date__range=[sixty, thirty], date_in=None)
    params['sixty'] = sixty_days

    #Grab the items that are sixty to ninety days overdue(60-89)
    ninety_days = hmod.RentalItem.objects.filter(due_date__range=[ninety, sixty], date_in=None)
    params['ninety'] = ninety_days

    # Grab the items that are ninety or more days overdue (90+)
    ninety_plus = hmod.RentalItem.objects.filter(due_date__range=['1900-01-01', ninety], date_in=None)
    params['ninety_plus'] = ninety_plus

    items = hmod.RentalItem.objects.filter(due_date__range=['1900-01-01', timezone.now()], date_in=None)

    #Grab the items that are thirty days overdue

    params['report_name'] = 'Overdue Rental Items'

    return templater.render_to_response(request, 'Report.html', params)

##########################################################################################
################### Batch Process to send emails to rentals overdue ######################
##########################################################################################

@view_function
@permission_required('base_app.add_item', login_url='/homepage/login/')
def email_overdue(request):

    # Define the view bag
    params={}

    items = hmod.RentalItem.objects.filter(due_date__range=['1900-01-01', '3000-01-01' ], date_in=None)
    users = []
    emails = []

    for item in items:
        try:
            user = hmod.User.objects.get(id=item.transaction.customer.id)
        except hmod.User.DoesNotExist:
            print('User does not exist.')

        if user not in users:
            users.append(user)

    for user in users:
        transactions = user.transaction_set.all()
        emails = []

        for trans in transactions:
            rental_items = trans.rentalitem_set.all()

            for item in rental_items:
                if item.due_date < datetime.date.today() and item.date_in is None:
                    emails.append(item)

        params['items'] = emails

        subject = "Items Overdue: Colonial Heritage Foundation"
        body = templater.render(request, 'overdue_email.html', params)
        send_mail(subject, body, 'brucehnsn@gmail.com', [request.user.email], html_message = body, fail_silently = False)

        params['users'] = users

        params['report_name'] = 'Overdue Rental Items'

        return templater.render_to_response(request, 'email_report.html', params)
