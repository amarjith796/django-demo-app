from django.shortcuts import render

from .models import Destination

# Create your views here.

def index (request):
    # dest1 = Destination()
    # dest1.id = 1
    # dest1.img = 'destination_1.jpg'
    # dest1.name = 'Bali'
    # dest1.price = 700
    # dest1.desc = 'Indonesian Capital'
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.id = 2
    # dest2.img = 'destination_2.jpg'
    # dest2.name = 'Mumbai'
    # dest2.price = 600
    # dest2.desc = 'Indian Rich City'
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.id = 3
    # dest3.name = 'Hyderabad'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 500
    # dest3.desc = 'Biryani and Sherwanai'
    # dest3.offer = False

    # destination = [dest1,dest2,dest3]
    destination = Destination.objects.all()

    return render(request, 'index.html', {'destination':destination})