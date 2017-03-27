from django.shortcuts import render
from cms.models import Pages
from django.http import HttpResponse


def show(request):
    content = Pages.objects.all()
    response = ""
    for entry in content:
        response = entry.name + ": " + entry.page + "<br>" + response
    return HttpResponse(response)


def entry(request, resource):
    try:
        entry = Pages.objects.get(name=resource)
        return HttpResponse(entry.page)
    except Pages.DoesNotExist:
        return HttpResponseNotFound('<h1>' + resource + ' not found.</h1>')
