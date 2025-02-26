# top_spotify_songs_api

Fetches a users top listened songs on spotify for a specified time frame.

## Introduction

This project utilizes Spotify's API and the Flask framework to redirect the user to a secure login page. After authentication, the app retrieves user information and displays their top songs on a simple webpage.

## Setup

Clone the repository:
```
git clone https://github.com/RLee2004/top_spotify_songs_api.git
```

Install necessary libraries:
```
pip install spotipy, os, time, flask, dotenv
```

### Create a Spotify Developer Application

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Log in with your Spotify account.
3. Click on 'Create App'.
4. Fill in the required details.
5. In 'Redirect URIs', enter:
```
http://127.0.0.1:5000/redirect
```
6. Once the app is created, click on the app and navigate to settings.
7. Here, you will find your `Client ID` and `Client Secret`. Copy these values

### Set Up Environment Variables
1. Create a `.env` file in the root of your project directory.
2. Add the following lines to the `.env` file, replacing the placeholders with your actual `Client ID` and `Client Secret`:
```
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```
Run using flask:
```
flask run
```

In app.py, you can change 'num_tracks' with the number of tracks to be displayed.
