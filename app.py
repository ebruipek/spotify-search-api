from flask import Flask, jsonify, abort, session
import random
import requests
from flask_cors import CORS, cross_origin
import spotify_api
import json

app = Flask(__name__)
app.secret_key = "randomSecretKey"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

genres =[]
with open('genres.json', 'r') as json_file:
    genres = json.load(json_file)

@app.route('/tracks/<genre>', methods=['GET'])
@cross_origin()
def get_tracks(genre):

    if genre in genres:
        picked_artist_name = random.choice(genres[genre])
    else:
        abort(404, 'Genre not found')
    
    token = spotify_api.auth()
 
    headers = {
        'Authorization': f"Bearer {token}",
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    return_object = []

    artist_info = spotify_api.search_by_artist_name(headers, picked_artist_name)
    artist_id = artist_info['artists']['items'][0]['id']
    
    tracks = spotify_api.get_artist_top_tracks(headers, artist_id)['tracks']
    for track in tracks:
        return_object.append({'artistName':picked_artist_name, 'trackName':track['name'], 'image':track['album']['images'][0]['url'] , 'previewUrl':track['preview_url']})
        
    return jsonify(return_object)
        
if __name__ == '__main__':
    app.run(host='0.0.0.0')
