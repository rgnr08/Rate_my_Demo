from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    # Request the context of the request
    # The context contains information such as the client's machine details, for example.

    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!

    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render_to_response('Rate_my_Demo/index.html', context_dict, context)

    #The following code was substituted by what's above
    #return HttpResponse("Rango says hello world! <a href='/rango/about'>about</a>")


def about(request):

    #return HttpResponse("Rango says: here is the about page blood! <a href='/rango/'>Index</a>")
    return render_to_response('Rate_my_Demo/about.html')