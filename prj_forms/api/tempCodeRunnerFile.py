def details(request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render())