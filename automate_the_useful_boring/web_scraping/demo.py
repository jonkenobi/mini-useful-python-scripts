import bs4
import requests

# downloading html
# res = requests.get('https://google.com')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print("There was a problem:{exc}")
# playFile = open('google-dot-com.html','wb')
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)
# playFile.close()

# exampleFile = open('google-dot-com.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile, features="lxml")
# print(type(exampleSoup))

import subprocess

subprocess.Popen('bye.txt')
