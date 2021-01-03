from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.

def home(request):
    return render (request, 'home/home.html')

def contact(request):
    if request.method == 'POST':
        fname = request.POST ['fname']
        lname = request.POST ['lname']
        email = request.POST ['email']
        query = request.POST ['query']
        # print(fname, lname, email, query)
        if len(fname)<3 or len(lname)<3 or len(email)<3 or len(query)<5:
            messages.warning(request, "Please fill in the correct information")
        else:
            contact = Contact(fname=fname, lname=lname, email=email, query=query)
            contact.save()
            messages.success(request, "Your Message has been sent sucessfully")
        # print("We are using Post Method")
    return render (request, 'home/contact.html')

def about(request):
    return render (request, 'home/about.html')

def search(request):
    return render (request, 'home/search.html')

def login(request):
    return render (request, 'home/login.html')