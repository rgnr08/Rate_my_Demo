Rate_my_Demo
============

Sofa King Good ITECH Project


DESCRIPTION AND MAIN FEATURES
===================================================================

Rate my Demo is a website that has been designed to deliver a unique music sharing platform where artists can submit demos to be listened to and rated by other users.

Key features of the site are the randomised delivery of audio tracks to users which means that users cannot just select and rate music by their favourite artists. This will help reduce bias in the demo ratings as users will only rate a random selection of tracks. A unique feature of the rating system is that users can upvote or downvote a demo as much as they are willing to.There is also a randomiser button that will re-randomise the list of demos that are available to users.

Artists will be able to upload demos, name them and add a thumbnail image for each one via the upload button.  They will also be able to delete any uploaded demos via their demo page.

Each demo can be rated up and down by users and these ratings will be visible to all users. The top five tracks will also be displayed on the home page and the user profile page.

Users will also be able to select favourite tracks which will allow them to listen to them at any time via a favourite page that is accessed from their profile page. Users can also remove favourites at any time via the favourite page.


ISSUES AND INCOMPLETE FEATURES
===================================================================

There are a number of issues remaining in the app that we would like to fix. There are also some features that were not implemented.


Issues:

1. The design is not responsive to changes in window sizes or use on small screens unless the zoom level is reduced. 

2. Adding a demo to favourites triggers a refresh the current selection of Demos.

3. It is possible for users to create another profile by going to the about page and clicking on the register button.

4. At the moment clicking play on another demo while one is already playing results in both songs playing at once. We would hope to implement a fix so that only one song would play at a time. 

Unimplemented features:

1. A feature to allow limited search based on genre was not implemented, but genre preference is stored in the users profile.

2. The ability to change profile details via the change details page was not implemented. Althogh the change details page is present it does not work and clcking any of the buttons returns users to the home page.

3. At the moment the user is unable to visually identify which song is currently playing. We would hope to add some form of visual indicator to solve this issue.


INSTALLATION
===================================================================

If Rate my Demo is cloned directly from Github it will contain the Rate_my_Demo.db file which will allow the site to be run immediately using the command python manage.py runserver. When this command has been run the default address to view the site locally is http://127.0.0.1:8000/Rate_my_Demo.

Below are the usernames and passwords for this version of Rate my Demo.

User        Pasword       Type
  
123         123         Admin

Jess        jess        Artist

Jean        jean        Artist

Jack        jack        Listener


To run a clean version of the Rate my Demo webapp simply delete the database and empty the media folder. Then run python manage.py syncdb to recreate the database. You will now be able repopulate Rate my Demo with new content and users. 
We did not create a populate script for the app as . 

