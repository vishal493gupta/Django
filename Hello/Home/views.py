from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context={
        'variable1':'God is great.',
        'variable2':'He is immortal.'
    }
    return render(request, 'index.html',context)
   # return HttpResponse("This is a Homepage.")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is a About page.")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is a Services page.")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your messages has been submitted !') 
        
    return render(request, 'contact.html')
    # return HttpResponse("This is a Contact page.")
    
def thali(request):
    return render(request, 'thali.html')

def fastfood(request):
    return render(request, 'fastfood.html')

def desserts(request):
    return render(request, 'desserts.html')

