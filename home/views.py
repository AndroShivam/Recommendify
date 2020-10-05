import spotipy
from django.shortcuts import render
from spotipy.oauth2 import SpotifyClientCredentials
from home.utils.api import SpotifyAPI
from home.utils.form import SearchForm

client_id  = 'your_client_id'
client_secret = 'your_client_secret'

ccm = spotipy.SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager = ccm)

spotify = SpotifyAPI(client_id = client_id, client_secret = client_secret)


def main_home(request):
    result = None
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            query_to_be_search = form.cleaned_data['search']
            query_result = spotify.search(query = query_to_be_search)
            items = query_result['artists']['items']
            artist_uri = items[0]['uri']
            result = sp.artist_related_artists(artist_uri)
    else:
        form = SearchForm()

    return render(request, 'home/home.html', {'form' : form, 'result' : result})