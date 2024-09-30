import os, sys
import requests
import geocoder
import matplotlib.pyplot as plt
from PIL import Image  #this is the FORK of native pillow

# Get user's location using IP and show him/her weather forecast
g = geocoder.ip('me')
lat, lon = g.latlng

accessKey = 'dcd4f1b0-b2c3-4b32-bfe2-c5f37c5f375c'
headers = {
    'X-Yandex-Weather-Key': accessKey
}

res = requests.get('https://api.weather.yandex.ru/v2/forecast?lat=' + str(lat) + '&lon=' + str(lon), headers=headers)

data = res.json()

print('temp: ', data['fact']['temp'])
print('season: ', data['fact']['season'])
print('cloudness: ', data['fact']['cloudness'])
print('feels_like: ', data['fact']['feels_like'])
print('humidity: ', data['fact']['humidity'])
print('pressure_mm: ', data['fact']['pressure_mm'])
print('uv_index: ', data['fact']['uv_index'])
print('wind_speed: ', data['fact']['wind_speed'])


# work with images

def convert(*args):
    for infile in args:
        f, e = os.path.splitext(infile)
        outfile = f + ".jpg"
        if infile != outfile:
            try:
                with Image.open(infile) as im:
                    im = im.convert('RGB')
                    im.save(outfile)
            except OSError:
                print("cannot convert", infile)


convert('tiger.png')


#mathPlot

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.