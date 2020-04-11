import requests
import json
lastfm_api = '63f12697373fab1778dd5247a10fe28a'
lstfm_url_request = requests.get('http://ws.audioscrobbler.com/2.0/?method=album.gettags&artist=cher&album=believe&api_key=63f12697373fab1778dd5247a10fe28a&format=json')

print(lstfm_url_request)

lastfm_url = 'http://ws.audioscrobbler.com/2.0/?method=album.gettags&artist=cher&album=believe&api_key=63f12697373fab1778dd5247a10fe28a&format=json'


