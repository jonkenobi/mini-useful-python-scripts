# !python 3
# tenki.py --- This program opens the OpenWeatherMap version of a cities weather

import webbrowser, sys

location = ' '.join(sys.argv[1:])
id = ''

if len(sys.argv) < 2:
    print('Usage: tenki.py location')
    input('')

if location == 'Vancouver':
    id = '6173331'
elif location == 'Tokyo':
    id = '1850147'
elif location == 'Taipei':
    id = '1668341'
url = 'https://openweathermap.org/city/' + id
webbrowser.open(url)
