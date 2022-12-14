from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def simple_view(request):
    return render(request, 'first_app/example.html')


def variable_view(request):

    my_var = {
        'first_name': 'Rosalind',
        'last_name': 'Franklin',
        'some_list': [1, 2, 3],
        'some_dict': {
            'inside_key': 'inside_value'
        }
    }

    return render(request, 'first_app/variable.html', context=my_var)
