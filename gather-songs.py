#!/usr/bin/env python

# Libraries
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace values
# client_id = 'client-id'
# client_secret = 'secret-id'

# Bring Playlist URL
# playlist_url = 'URL_DE_LA_PLAYLIST'
playlist_url = 'https://open.spotify.com/playlist/7fMPE0wQvfsnxe1NWMsufK?si=2670aee6143d417f'

def get_spotify_tracks(playlist_url):
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

    playlist_id = playlist_url.split('/')[-1]
    results = sp.playlist_tracks(playlist_id)

    tracks = []
    for item in results['items']:
        track_info = item['track']
        track_name = track_info['name']
        artists = [artist['name'] for artist in track_info['artists']]
        album = track_info['album']['name']
        spotify_link = track_info['external_urls']['spotify']

        tracks.append({'track_name': track_name, 'artists': artists, 'album': album, 'spotify_link': spotify_link})

    return tracks

if __name__ == '__main__':
    tracks = get_spotify_tracks(playlist_url)
    for track in tracks:
        print(f"Track: {track['track_name']} | Artists: {', '.join(track['artists'])} | Album: {track['album']} | Spotify Link: {track['spotify_link']}")

