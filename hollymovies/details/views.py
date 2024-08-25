# details/views.py

from django.http import HttpResponse

def myInformation(request):
    name = "Indrek Kuusk"  # Replace with your actual name
    age = 50  # Replace with your actual age
    return HttpResponse(f"My name is {name} and I'm {age} years old.")

# details/views.py


