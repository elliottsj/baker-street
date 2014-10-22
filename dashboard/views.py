from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext


def index(request):
    template = loader.get_template('dashboard/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
