# !python3
#tenki.py ----Opens accuweather webpage for specified locations,  using googles search results
#Usage: tenki.py {location} ---open weather forecast page for that location
       #tenki.py hour {location} --- open hourly forecast page
import requests, sys, webbrowser, bs4
if len(sys.argv)== 1:
    print('''Usage: tenki.py {location} ---open weather forecast page for that location
       tenki.py hour {location} --- open hourly forecast page''')
    input()
    sys.exit()
if sys.argv[1].lower()in ['hour','hourly','hr']:
    print('Googling hourly weather for {} .....'.format(' '.join(sys.argv[2:]).capitalize()))  # display text while downloading Google page
    res = requests.get('https://google.com/search?q=AccuWeather hourly ' + ' '.join(sys.argv[2:]))
else:
    print('Googling weather for {} .....'.format(' '.join(sys.argv[1:]).capitalize()))  #  display text while downloading Google page
    res = requests.get('https://google.com/search?q=AccuWeather' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#  Retrieve Top Search links
soup = bs4.BeautifulSoup(res.text)

linkelems = soup.select('.r a')
#open first result
webbrowser.open('https://google.com' + linkelems[0].get('href'))