from django.template import RequestContext
from django.shortcuts import render_to_response
from Rate_my_Demo.forms import UserForm, RateMyDemoUserForm, DemoForm, FavForm
from Rate_my_Demo.models import Demo, RateMyDemoUser, Favourites
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.urlresolvers import reverse



def index(request):


    sorts = Demo.objects.order_by('-up')[:5]
    demos = Demo.objects.order_by('?')

    return render_to_response('Rate_my_Demo/index.html', {'demos': demos, 'sorts': sorts},  context_instance=RequestContext(request))


def home(request):
    context = RequestContext(request)
    rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
    demos = Demo.objects.all()


    return render_to_response('Rate_my_Demo/home.html', {'demos': demos, 'rate_my_demo_user': rate_my_demo_user},  context)

def about(request):


    return render_to_response('Rate_my_Demo/about_page.html')



def register(request):

    context = RequestContext(request)


    registered = False


    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = RateMyDemoUserForm(data=request.POST)

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

            if registered == True:
                return render_to_response('Rate_my_Demo/registration_successful.html')

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
            'Rate_my_Demo/register_page.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


def upload(request):
    # Handle file upload

    uploaded = False
    if request.method == 'POST':
        form = DemoForm(request.POST, request.FILES)



        if form.is_valid():
            print "got here"

            rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
            print rate_my_demo_user

            newdemo = Demo()
            newdemo.img = request.FILES['img']
            newdemo.user = rate_my_demo_user
            newdemo.docfile = request.FILES['docfile']
            newdemo.genre = request.POST['genre']
            newdemo.title = request.POST['title']
            newdemo.up = request.POST['up']
            newdemo.down = request.POST['down']
            newdemo.save()
            uploaded = True

            if rate_my_demo_user.usertype == 'Artist':
                print 'user is an artist'
                demos = Demo.objects.all()
                return HttpResponseRedirect('/Rate_my_Demo/artist/', {'uploaded': uploaded, 'demos': demos})
            else:
                print 'user is listener!!'
                demos = Demo.objects.all()
                return render_to_response('/Rate_my_Demo/listener/', {'uploaded': uploaded, 'demos': demos})




    else:
        form = DemoForm() # A empty, unbound form

    rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
    demos = Demo.objects.filter(user=rate_my_demo_user)

    print demos


    return render_to_response(
        'Rate_my_Demo/upload_page.html',
        {'demos': demos, 'form': form},
        context_instance=RequestContext(request)
    )



def user_login(request):
    #uploader = request.user
    #demos = Demos.objects.filter(user = uploader)

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

                rate_my_demo_user = RateMyDemoUser.objects.get(user = user)
                print rate_my_demo_user.usertype

                if rate_my_demo_user.usertype == 'Artist':
                    print 'user is an artist'
                    demos = Demo.objects.all()
                    return HttpResponseRedirect('/Rate_my_Demo/artist/', {'demos': demos})
                else:
                    print 'user is listener!!'
                    demos = Demo.objects.all()
                    return HttpResponseRedirect('/Rate_my_Demo/listener/', {'demos': demos})
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rate my Demo account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return render_to_response('Rate_my_Demo/bad_details.html')

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('Rate_my_Demo/login_page.html', {}, context)



@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/Rate_my_Demo/')


@login_required
def artist(request):

    context = RequestContext(request)
    if request.method == 'POST':
        form=FavForm(data=request.POST)


        rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
        favdemo = Demo.objects.get(title=request.POST['demo'])

        newfav=Favourites()
        newfav.user=rate_my_demo_user
        newfav.demo=favdemo
        newfav.save()

        demos = Demo.objects.all()
        sorts = Demo.objects.order_by('-up')[:5]

        return HttpResponseRedirect('/Rate_my_Demo/artist/',{'demos': demos, 'form': form, 'sorts':sorts},context)



    else:

        rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
        form = FavForm(request.POST)
        demos = Demo.objects.order_by('?')
        sorts = Demo.objects.order_by('-up')[:5]


        return render_to_response('Rate_my_Demo/artist.html', {'demos': demos, 'form': form, 'rate_my_demo_user': rate_my_demo_user, 'sorts':sorts}, context)



@login_required
def listener(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form=FavForm(data=request.POST)


        rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
        favdemo = Demo.objects.get(title=request.POST['demo'])

        newfav=Favourites()
        newfav.user = rate_my_demo_user
        newfav.demo= favdemo
        newfav.save()

        demos = Demo.objects.order_by('?')
        sorts = Demo.objects.order_by('-up')[:5]


        return HttpResponseRedirect('/Rate_my_Demo/listener/', {'demos': demos, 'form': form, 'sorts': sorts}, context)



    else:
        print "METHOD IS NOT POST!"

        rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
        form = FavForm(request.POST)

        demos = Demo.objects.order_by('?')

        sorts = Demo.objects.order_by('-up')[:5]

        demos = Demo.objects.order_by('?')
        return render_to_response('Rate_my_Demo/listener.html', {'demos': demos, 'form': form, 'rate_my_demo_user': rate_my_demo_user, 'sorts':sorts}, context)


@login_required
def check_usertype(request):

    user = request.user
    print user.username

    RMDuser = RateMyDemoUser.objects.get(user=user)
    print RMDuser.usertype

    if RMDuser.usertype == 'Artist':
        print 'user is an artist'
        demos = Demo.objects.all()
        return HttpResponseRedirect('/Rate_my_Demo/artist/', {'demos': demos})
    else:
        print 'user is listener!!'
        demos = Demo.objects.all()
        return HttpResponseRedirect('/Rate_my_Demo/listener/', {'demos': demos})


def reg_success(request):

    return HttpResponseRedirect('/Rate_my_Demo/registration_successful.html/')


def contact(request):

    return render_to_response('Rate_my_Demo/contact.html')


def demos(request):
    if request.method == 'POST':

        demo = request.POST['demo']
        print demo

        todel = Demo.objects.filter(id=demo)

        todel.delete()

        rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
        demos = Favourites.objects.filter(user=rate_my_demo_user)

        return HttpResponseRedirect('/Rate_my_Demo/demos/', {'demos': demos, 'rate_my_demo_user': rate_my_demo_user})

    else:

        rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
        demos = Demo.objects.filter(user=rate_my_demo_user)



    return render_to_response('Rate_my_Demo/demos.html', {'demos': demos, 'rate_my_demo_user': rate_my_demo_user}, context_instance=RequestContext(request))


def favourites(request):
    user = request.user
    RMDuser = RateMyDemoUser.objects.get(user=user)

    if request.method == 'POST':
        fav = request.POST['fav']

        todel = Favourites.objects.filter(id=fav)

        todel.delete()

        rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
        favs = Favourites.objects.filter(user=rate_my_demo_user)

        if RMDuser.usertype == 'Artist':

            return render_to_response('Rate_my_Demo/favourites.html', {'favs': favs, 'rate_my_demo_user': rate_my_demo_user}, context_instance=RequestContext(request))

        else:

            return render_to_response('Rate_my_Demo/listener_favourites.html', {'favs': favs, 'rate_my_demo_user': rate_my_demo_user}, context_instance=RequestContext(request))

    else:
        rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
        favs = Favourites.objects.filter(user=rate_my_demo_user)

        return render_to_response('Rate_my_Demo/favourites.html', {'favs': favs, 'rate_my_demo_user': rate_my_demo_user}, context_instance=RequestContext(request))


def listener_favourites(request):

    if request.method == 'POST':
        fav = request.POST['fav']

        todel = Favourites.objects.filter(id=fav)

        todel.delete()

        rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
        favs = Favourites.objects.filter(user=rate_my_demo_user)

        return render_to_response('Rate_my_Demo/listener_favourites.html', {'favs': favs, 'rate_my_demo_user': rate_my_demo_user}, context_instance=RequestContext(request))

    else:
        rate_my_demo_user = RateMyDemoUser.objects.get(user=request.user)
        favs = Favourites.objects.filter(user=rate_my_demo_user)

        return render_to_response('Rate_my_Demo/listener_favourites.html', {'favs': favs, 'rate_my_demo_user': rate_my_demo_user}, context_instance=RequestContext(request))


def user_details(request):

    return render_to_response('Rate_my_Demo/user_details.html')

@login_required
def like_demo(request):

    context = RequestContext(request)
    demo_id = None

    if request.method == 'GET':

        print request.GET
        demo_id = request.GET['demo_id']
        print demo_id

    likes = 0
    if demo_id:
        demo = Demo.objects.get(id=int(demo_id))
        if demo:
            likes = demo.up + 1
            demo.up = likes
            demo.save()

    return HttpResponse(likes)

@login_required
def unlike_demo(request):
    context = RequestContext(request)
    demo_id2 = None

    if request.method == 'GET':

        demo_id2 = request.GET['demo_id2']

    unlikes = 0
    if demo_id2:
        demo = Demo.objects.get(id=int(demo_id2))
        if demo:
            unlikes = demo.down + 1
            demo.down = unlikes
            demo.save()

    return HttpResponse(unlikes)


