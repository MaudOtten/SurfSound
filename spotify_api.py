#!/usr/bin/python3

import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests

from exceptions import ResponseException
from secrets import spotify_token, spotify_user_id
#from example_songs import Song1, Song2

class CreatePlaylist:
    def __init__(self):
        # Get your starting info (Spotify)
        self.playlist_name = 'SurfSound'
        self.all_song_info = {}

    def create_playlist(self):
        """Create A New Playlist"""
        request_body = json.dumps({
        "name": self.playlist_name,
        "description": "Jam to the sounds of your surfing history!",
        "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)
        response = requests.post(
        query,
        data=request_body,
        headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(spotify_token)
        }
        )
        response_json = response.json()

        # playlist id
        return response_json["id"]

    def get_spotify_uri(self, song_name):
        """Search For the Song"""
        query = "https://api.spotify.com/v1/search?query=track%3A{}&type=track&offset=0&limit=20".format(
        song_name
        )
        response = requests.get(
        query,
        headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(spotify_token)
        }
        )

        response_json = response.json()

        songs = response_json["tracks"]["items"]

        if response_json["tracks"]["items"] != []:
            songs = response_json["tracks"]["items"]
            # only use the first song, return uri
            return songs[0]["uri"]
        else:
            # else return null
            return 0

    def check_playlist(self):
        response = requests.get(
            'https://api.spotify.com/v1/users/{}/playlists'.format(spotify_user_id),
            headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
            }
            )

        allplaylists = [info for playlist, info in response.json().items()]
        print(allplaylists)
        idx = [names['id'] for names in allplaylists[1] if names['name'] == self.playlist_name]

        if not idx:
            playlist_exists = 0
            playlist_id = 0
        else:
            playlist_exists = 1
            playlist_id = idx[0]

        return playlist_exists, playlist_id

    def add_song_to_playlist(self):
        """Add all liked songs into a new Spotify playlist"""
        # populate dictionary with our liked songs
        #self.get_liked_videos()

        keywords = ['anananaanan', 'postnord', 'Like', 'What the fuck', 'good as hell', 'cute cats']

        urs = [self.get_spotify_uri(keyword) for keyword in keywords]
        uris = [i for i in urs if i is not 0]

        # create a new playlist
        playlist_exists, playlist_id = self.check_playlist()

        if not playlist_exists:
            playlist_id = self.create_playlist()
        else:
            response = requests.get(
                'https://api.spotify.com/v1/playlists/{}/tracks'.format(playlist_id),
                headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
                }
                )
            print(response.json().items())

        # add all songs into new playlist
        request_data = json.dumps(uris)
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlist_id)

        response = requests.post(
            query,
            data=request_data,
            headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
            }
        )

        # check for valid response status
        if response.status_code != (200 and 201):# or 201):
            raise Warning(response.status_code)


        response_json = response.json()
        return response_json

print(__name__)
if __name__ == '__main__':
    cp = CreatePlaylist()
    cp.add_song_to_playlist()
