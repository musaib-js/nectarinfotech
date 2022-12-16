from django.shortcuts import render, redirect
from .models import Contact, Testimonial
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def home(request):
    testimonials = Testimonial.objects.all()
    context = {'testimonials': testimonials}
    return render(request, 'index2.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']

        if len(name) < 5 or len(phone)<10 or len(message)<20:
            messages.error(request, "Fill the form correctly")

        newcontact = Contact(name = name, phone = phone, message = message)
        newcontact.save()
        messages.success(request, "Your Details Have Been Submittted Successfully. We'll Get Back To You Soon")

    return redirect('/')

def clients(request):
    return render(request, 'clients.html')

def error_404_view(request, exception):
    return render(request, '404.html')