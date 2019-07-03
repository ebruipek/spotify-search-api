from flask import Flask, jsonify, abort
import requests

# Spotify Api Endpoints
TOKEN_URL = 'https://accounts.spotify.com/api/token'
SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'
TOP_TRACKS_ENDPOINT = 'https://api.spotify.com/v1/artists/{id}/top-tracks'

# Client info
CLIENT_ID = 'af40213fd82947a2b595787864b41adb'
CLIENT_SECRET = '95c586b5d4314bb9b4980ad5e4d4c14b'

def search_by_artist_name(headers, artist_name):
    payload = {'q': artist_name, 'type': 'artist', 'limit': '1'}
    res = requests.get(SEARCH_ENDPOINT, params=payload, headers=headers)
    res_data = res.json()
    
    artists = res_data.get('artists')
    items = artists['items']
    if not artists or not items or res.status_code != 200:
        app.logger.error(
            'Failed to get artist: %s,%s,%s',
            artist_name,res_data.get('error'),
            res_data.get('error_description')
        )
        abort(400)
    return res_data

def get_artist_top_tracks(headers, artist_id):
    url = TOP_TRACKS_ENDPOINT.format(id=artist_id)
    payload = {'limit': '50', 'country': 'US'}
    res = requests.get(url, params=payload, headers=headers)
    
    res_data = res.json()
    
    tracks = res_data.get('tracks')
    if not tracks or res.status_code != 200:
        app.logger.error(
            'Failed to get tracks: %s,%s',
            res_data.get('error'),
            res_data.get('error_description')
        )
        abort(400)
    return res_data
    
def auth():
 
    payload = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'grant_type': 'client_credentials',
    }

    res = requests.post(TOKEN_URL, auth=(CLIENT_ID, CLIENT_SECRET), data=payload)
    res_data = res.json()

    access_token = res_data.get('access_token')

    if not access_token or res.status_code != 200:
        app.logger.error(
            'Failed to get access token: %s, %s',
            res_data.get('error'),
            res_data.get('error_description'),
        )
        abort(400)
    else:
        return access_token
