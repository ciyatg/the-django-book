from django.http import HttpResponse #We import the class HttpResponse, which lives in the django.http module
import datetime

def hello(request): #We define a function called hello – the view function
    return HttpResponse("Hello world") #Each view function takes at least one parameter, called request by convention.

def current_datetime(request): #The new current_datetime function calculates the current date and time, as a datetime.datetime object, and stores that as the local variable now.
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now #This constructs an HTML response using Python’s “format-string” capability.        
    return HttpResponse(html) #Finally, the view returns an HttpResponse object that contains the generated response.
