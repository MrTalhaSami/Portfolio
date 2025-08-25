from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .models import dataClass


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
        date = request.POST.get('date')
        
        dataClass.objects.create(
            firstName = fisrt,
            lastName = last,
            number = numb,
            email = email,
            message = msg,
            date = date,
        )
        return redirect('success')
        
    return render(request,'form.html')

def success(request):
    return render(request, 'success.html')





