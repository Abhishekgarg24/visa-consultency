from django.shortcuts import render
from userside.models import Contact
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        adh = request.POST.get('adh')
        req = request.POST.get('req')
        contacts = Contact(name=name,phone=phone,adh=adh,req=req)
        #Contacts = contacts(phone=phone, adh=adh, req=req)
        contacts.save()
    return render(request,'contact.html')
def germany(request):
    return render(request,'germany.html')
def australia(request):
    return render(request,'australia.html')
def canada(request):
    return render(request,'canada.html')