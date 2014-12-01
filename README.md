SpotiCover
==========

SpotiCover is a personal project using the Spotify API to create posters and banners using the album/single covers of the user songs on Spotify. The user can also choose to create a poster from his most listened to songs.

I use pyspotify to connect to the user Spotify account and to download the covers. Then I use Pillow, the python image library to produce a final image.

The script that allows to do all this is spoticover.py

The web app using flask is not finished yet.

Linux :

    apt-get install libspotify-dev

Mac OS X :

    brew install libspotify
