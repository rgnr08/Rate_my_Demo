from Rate_my_Demo.models import RateMyDemoUser, Demo,

def add_user(user, thumbnail, favourite_genres, location, favourites, uploaded_demos, is_artist):
    u = RateMyDemoUser.objects.get_or_create(user, )
