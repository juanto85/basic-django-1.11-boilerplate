import random
from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

# Function based view
def home(request):
    num = random.randint(0, 45)
    return render(request, "layout.html", {"var1": "Yo soy la variable", "num": num,}) #response
