# ---- UrlLi Request Example ----

from urllib.request import urlopen

with urlopen('http://localhost:3000/lyrics/') as response:
  
  # Use the correct function to read the response data from the response object
  data = response.read()
  encoding = response.headers.get_content_charset()

  # Decode the response data so you can print it as a string later
  string = data.decode(encoding)
  
  print(string)

# ---- Request Example ----

import requests

response = requests.get('http://localhost:3000/lyrics')

print(response.text)

# ---- Constructing a URL with parameters ----

query_params = {'artist': 'Deep Purple', 'include_track' : True}

response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

print(response.url)

print(response.text)

# ---- Creating and deleting resources using an API ----

playlist_data = {'Name': 'Rock Ballads'}

response = requests.post('http://localhost:3000/playlists', data=playlist_data)

print(response.text)

# ---- Deleting a resource ----

requests.delete('http://localhost:3000/playlists/2')

# Get the list of all existing playlists again
response = requests.get('http://localhost:3000/playlists')
print(response.text)


# ---- Response codes and APIs ----

response = requests.get('http://localhost:3000/movies')

if(response.status_code == requests.codes.ok):
  print('The server responded succesfully!')
  
elif (response.status_code == requests.codes.not_found):
  print('Oops, that API could not be found!')


# ---- Using request and response headers ----

print(response.headers['accept'])

headers = {'accept': 'application/json'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

print(response.text)

# ---- Handling content-types errors ----

headers = {'accept': 'appplication/xml'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

if response.status_code == 406:
  print('The server cannot provide the requested content type.')
  print('These are the content types the server accepts: ' + response.headers['accept'])

else:
  print(response.text)

# ---- Basic Authentication with requests ----

response = requests.get('http://localhost:3000/albums')

if(response.status_code == 200):
    print("Success!")

elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')

# ---- Basic Authentication with requests using a tuple ----

authentication = ('john@doe.com', 'Warp_ExtrapolationsForfeited2')

response = requests.get('http://localhost:3000/albums', auth=authentication)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')

# ---- API key authentication with requests ----

headers = {'Authorization': 'Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'}

response = requests.get('http://localhost:3000/albums', headers=headers)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')

# ---- Receiving JSON with the requests package ----

headers = {'Authorization': 'Bearer ' + API_TOKEN, 'Accept': 'application/json'}

response = requests.get('http://localhost:3000/albums/1/', headers=headers)

album = response.json()

print(album['Title'])

# ---- Sending JSON with the requests package ----

playlists = [{"Name":"Rock ballads"}, {"Name":"My favorite songs"}, {"Name":"Road Trip"}]

requests.post('http://localhost:3000/playlists/', json=playlists)

response = requests.get('http://localhost:3000/playlists')

print(response.text)

# ---- Handling errors with Requests ----

from requests.exceptions import ConnectionError

url ="http://wronghost:3000/albums"

try:
   r = requests.get(url)
   print(r.text)

except ConnectionError as e:
   print(f"Connection error: {e}."

#  ---- Handling errors with Requests ----

from requests.exceptions import HTTPError

url ="http://localhost:3000/albums/"

try: 
    r = requests.get(url) 
    r.raise_for_status()
    print(r.status_code)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')


# ---- API LIMITS ----

while True:
    params = {'page': page_number, 'per_page': 500}
    response = requests.get('http://localhost:3000/tracks', params=params, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    
    print(f'Fetching tracks page {page_number}')

    if len(response_data['results']) == 0:
        break

    for track in response_data['results']:
        if(track['Length'] > longestTrackLength):
            longestTrackLength = track['Length']
            longestTrackTitle = track['Name']

    page_number = page_number + 1
 
    time.sleep(3) # to respect the API limits

    
print('The longest track in my music library is: ' + longestTrackTitle)


