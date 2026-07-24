from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .models import dataClass
from django.core.exceptions import ValidationError
import re



# Create your views here.

def response(request):
    return HttpResponse("Server is working...")

def landing(request):
    return render(request, 'landing.html')

def projects(request):
    return render(request, 'projects.html')

def experience(request):
    return render(request, 'experience.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def blog(request):
    return render(request, 'blog.html')

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
    return render(request, 'about.html')

#form Logic:

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        msg = request.POST.get('message', '').strip()

        #Validations for form
        errors = []

        if not re.fullmatch(r"[A-Za-z ]+", name):
            errors.append("Name should only contain letters and spaces.")

        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Invalid email format.")

        if not msg:
            errors.append("Message cannot be empty.")

        if errors:
            return render(request, 'form.html', {'errors': errors})


        dataClass.objects.create(
            firstName = name,
            email = email,
            message = msg,
        )
        return redirect('success')

    return render(request,'form.html')

def success(request):
    return render(request, 'success.html')





