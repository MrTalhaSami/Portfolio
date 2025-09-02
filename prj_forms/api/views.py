from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .models import dataClass
from django.core.exceptions import ValidationError
import re



# Create your views here.

def response(request):
    return HttpResponse("Server is working...")

def landing(request):
    template = loader.get_template('landing.html')
    return HttpResponse(template.render())
    
def members(request):
    template = loader.get_template('members.html')
    data = dataClass.objects.all().values()
    context = {
        "data" : data,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
  data = dataClass.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'data': data,
  }
  return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

#form Logic:

def form(request):
    if request.method == 'POST':
        fisrt = request.POST.get('fName')
        last = request.POST.get('lName')
        numb = request.POST.get('num')
        email = request.POST.get('email')
        msg = request.POST.get('message')

        
        #Validations for forms
        errors = []
        
        #for Number input
        if not re.fullmatch(r"\d{11}", numb):
            errors.append("number must be 11 digits")
        
        #for email input
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Invalid email format.")
            
        #for first and last name
        if not re.fullmatch(r"[A-Za-z]+", fisrt):
            errors.append("First name should only contain letters.")
        if not re.fullmatch(r"[A-Za-z]+", last):
            errors.append("Last name should only contain letters.")
            
        if errors:
            return render(request, 'form.html', {'errors': errors})
        
        
        dataClass.objects.create(
            firstName = fisrt,
            lastName = last,
            number = numb,
            email = email,
            message = msg,
        )
        return redirect('success')
        
    return render(request,'form.html')

def success(request):
    return render(request, 'success.html')





