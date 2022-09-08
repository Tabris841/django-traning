from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def simple_view(request):
    return render(request, 'first_app/example.html')
