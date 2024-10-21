

from django.shortcuts import redirect, render
from django.http import HttpResponse
from contact_info.models import Contact


def index(request):


    # Contact form
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    # end of contact form

    return render(request, 'index.html', {
        'contact': contact
    })