from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import World

def home(request):
    return render(request, 'worlds/home.html')

@login_required
def my_worlds(request):
    worlds = World.objects.filter(owner=request.user)
    return render(request, 'worlds/my_worlds.html', {'worlds': worlds})