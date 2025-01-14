import spotipy, os, time
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

num_tracks = 20

app.secret_key = os.urandom(12)
app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'

def create_spotify_oauth():
    return SpotifyOAuth(client_id, 
                        client_secret, 
                        redirect_uri= url_for('redirect_page', _external = True),
                        scope="user-top-read",
                        show_dialog=True)

@app.route('/')
# Redirects the user to sign in with Spotify
def index():
    session.clear()
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirect_page():
    session.clear()
    code = request.args.get('code')
    print(f"Received code: {code}")

    token_info = create_spotify_oauth().get_access_token(code)

    # Clear the session before setting the new token info
    session["token_info"] = token_info
    print("Token Info:", token_info)
    return render_template('index.html')

@app.route('/getTopTracks/<time_range>')
def getTopTracks(time_range):
    try: 
        # get the token info from the session
        token_info = getToken()
    except:
        # if the token info is not found, redirect the user to the login route
        print('User not logged in')
        return redirect("/")
    
    access_token = token_info["access_token"]
    sp = spotipy.Spotify(access_token)
    
    top_tracks_dict = sp.current_user_top_tracks(num_tracks, time_range=time_range)
    top_tracks = [f"{i + 1}. {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}" for i, track in enumerate(top_tracks_dict["items"])]
    formatted = "<br>".join(top_tracks)

    return formatted

def getToken():
    token_info = session.get('token_info', None)
    if not token_info:
        # if the token info is not found, redirect the user to the login route
        return redirect(url_for('login', _external=False))
    
    # check if the token is expired and refresh it if necessary
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60

    if(is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])

    return token_info


