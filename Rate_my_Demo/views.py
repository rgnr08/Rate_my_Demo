from django.template import RequestContext
from django.shortcuts import render_to_response
from Rate_my_Demo.forms import UserForm, RateMyDemoUserForm, DemoForm
from Rate_my_Demo.models import Demo
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.urlresolvers import reverse



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
    return render_to_response('Rate_my_Demo/about_page.html')



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
            if 'thumbnail' in request.FILES:
                profile.thumbnail = request.FILES['thumbnail']

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


def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DemoForm(request.POST, request.FILES)
        # art = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            print "poopoerz"
            # newimg = Image(image = request.FILES['image'])
            # newimg.save()
            # print "image saved"
            newdemo = Demo()
            newdemo.img = request.FILES['img']
            newdemo.user = request.user.username
            print newdemo.user
            # newdoc = Document(docfile= request.FILES['docfile'], genre=request.POST['genre'], title=request.POST['title'], up=request.POST['up'], down=request.POST['down'], img = newimg)
            newdemo.docfile = request.FILES['docfile']
            newdemo.genre = request.POST['genre']
            newdemo.title = request.POST['title']
            newdemo.up = request.POST['up']
            newdemo.down = request.POST['down']
            # newdoc.img = newimg
            newdemo.save()



            print "HERE"
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('Rate_my_Demo.views.upload'))
    else:
        form = DemoForm() # A empty, unbound form
        # art = ImageForm()
    # Load documents for the list page
    demos = Demo.objects.all()
    # images = Image.objects.all()


    # Render list page with the documents and the form
    return render_to_response(
        'Rate_my_Demo/upload.html',
        {'demos': demos, 'form': form},
        context_instance=RequestContext(request)
    )



def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    print "HERE1"
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        print "HERE2"
        username = request.POST['username']
        print "HERE3"
        password = request.POST['password']

        print username
        print password
        print "HERE"
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
        return render_to_response('Rate_my_Demo/login_page.html', {}, context)

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