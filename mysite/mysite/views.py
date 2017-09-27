from django.http import HttpResponse #We import the class HttpResponse, which lives in the django.http module

def hello(request): #We define a function called hello – the view function
    return HttpResponse("Hello world") #Each view function takes at least one parameter, called request by convention.
