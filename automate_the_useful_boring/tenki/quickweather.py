# !python3
# quickweather.py -- Prints the weather for a location from the command line

import json, requests, sys, webbrowser

#compute location from sys arg
if  len(sys.argv) < 2:
    print('Usage: quickweather.py location')
    input('')
location = ' '.join(sys.argv[1:])
#if location.lower() = 'vancouver'
        #loc_id = 6173331
#There are two types of weather API : weather (for current weather) and  forecast ( for 3 hr interval 5 day forecast)
#url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=9c5d101d9349519943c3686340c57b15' % (location)
url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=9c5d101d9349519943c3686340c57b15'.format(location)
response = requests.get(url)
response.raise_for_status()

#Load Json data into Python variable
weatherdata = json.loads(response.text)
w = weatherdata['list']

# Print weather descriptions.
w = weatherdata['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
