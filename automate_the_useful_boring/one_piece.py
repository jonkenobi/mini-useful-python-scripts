#  !python3
# This program demonstrates downloading multiple images from  consecutive pages of a website
import requests, os , bs4
url = 'Some Manga site url'
os.makedirs('D:\\OnePiece_Downloads', exist_ok= True)
id = 'curPic'

while not url.endswith('#'):
    #Download the page
    print('Downloading page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    #Find the url of the image.
    comicElem = soup.select('#curPic')
    if comicElem == []:
        print('Could not find image')
    else:
        #TODO: See why the 'src' downloaded from soup is that simplified version
        comicurl = 'http:' + comicElem[0].get('src')
        print("Downloading image %s ..." %(comicurl))
        res = requests.get('comicurl')
        res.raise_for_status()
        # Save the image
        imageFile = open(os.path.join('OnePiece', os.path.basename(comicurl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    break
    #  TODO: Get the next pages URL
    prev = soup.select('a[rel = "prev"]')[0]
    # url =

