import os

def populate():
    rmd_user = add_user('JohnDoe',  )



def add_user(user, thumbnail, favourite_genres, location, favourites, uploaded_demos, artist):

    u = RateMyDemoUser.objects.get_or_create(user=user, thumbnail=thumbnail, favourite_genres=favourite_genres, location=location,
                                                favourites=favourites, uploaded_demos=uploaded_demos, artist=artist)[0]
    return u

def add_demo(name, file, duration, upload_time, uploader, artwork, up_votes, down_votes, genre, is_thumbs_up):

    d = Demo.objects.get_or_create(name=name, file=file, duration=duration, upload_time=upload_time, uploader=uploader,
                                   artwork=artwork, up_votes=up_votes, down_votes=down_votes, genre=genre, is_thumbs_up=is_thumbs_up)[0]
    return d

# Start execution here!

if __name__=='__main__':
    print"Starting Rate my Demo population script bravs..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

    from Rate_my_Demo.models import Demo, RateMyDemoUser
    populate()


