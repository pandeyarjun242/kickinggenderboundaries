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
        response = Response()
        response.name = request.user
        response.email = request.POST["email"]
        response.city = request.POST["city"]
        response.experience = request.POST["experience"]
        response.save()
        return redirect('home')
    else:
        return render(request, "contact.html")
