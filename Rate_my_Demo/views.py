from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from Rate_my_Demo.forms import UserForm, RateMyDemoUserForm, DemoForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout




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



def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = RateMyDemoUserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = RateMyDemoUserForm()

    # Render the template depending on the context.
    return render_to_response(
            'Rate_my_Demo/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

@login_required
def upload(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    uploaded = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        demo = DemoForm(data=request.POST)

        # If the two forms are valid...
        if DemoForm.is_valid(demo):

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'artwork' in request.FILES and 'file' in request.FILES:
                DemoForm.artwork = request.FILES['picture']
                DemoForm.file = request.FILES['picture']

                # Now we save the UserProfile model instance.
                DemoForm.save(demo)

            # Update our variable to tell the template registration was successful.
            uploaded = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print DemoForm.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        demo = DemoForm()

    # Render the template depending on the context.
    return render_to_response(
            'Rate_my_Demo/upload.html',
            {'demo' : demo, 'uploaded': uploaded },
            context)


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/Rate_my_Demo/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rate my Demo account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('Rate_my_Demo/login.html', {}, context)

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/Rate_my_Demo/')