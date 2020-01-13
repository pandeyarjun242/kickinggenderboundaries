from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Locations
from .models import Events
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def dashboard(request):
    locations = Locations.objects
    return render(request, 'dashboard.html', {'locations':locations})
@login_required
def events(request):
    events  = Events.objects
    return render(request, 'events.html', {'events':events})
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']
            Football_Experience = form.cleaned_data['Football_Experience']
            try:
                send_mail(name, Football_Experience, email, ['apandey@jpischool.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})
