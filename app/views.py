from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import Location
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def get_location(request):
    ip_address = request.META.get('REMOTE_ADDR')
    
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    data = response.json()
   
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        if latitude and longitude:
            location = Location(latitude=latitude, longitude=longitude)
            location.save()
            return render(request, 'location_success.html', {'latitude': latitude, 'longitude': longitude})
        else:
            return render(request, 'get_location.html', {'error': 'Latitude and Longitude are required'})
    return render(request, 'get_location.html')



from django.shortcuts import render
from .models import Location

@login_required
def location_list(request):
    locations = Location.objects.all().order_by('-timestamp')  # Assuming 'created_at' is the field representing creation date
    return render(request, 'location_list.html', {'locations': locations})



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('location_list')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')