import spotipy
from django.shortcuts import render
from spotipy.oauth2 import SpotifyClientCredentials
from home.utils.api import SpotifyAPI

client_id = 'your_client_id'
client_secret = 'your_client_secret'

ccm = spotipy.SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager = ccm)



def main_home(request):

    query_to_be_search = request.POST.get('search', None)

    if query_to_be_search is None or "":
        return render(request, 'home/home.html', {'result' : None})

    else:
        spotify = SpotifyAPI(client_id = client_id, client_secret = client_secret)
        query_result = spotify.search(query = query_to_be_search)
        items = query_result['artists']['items']
        artist_uri = items[0]['uri']
        result = sp.artist_related_artists(artist_uri)

    return render(request, 'home/home.html', {'result' : result})
