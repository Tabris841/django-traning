from django.http import HttpResponse, HttpRequest


def home_view(request: HttpRequest):
    return HttpResponse('Home Page')
