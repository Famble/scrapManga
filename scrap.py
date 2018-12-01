
#https://chrisalbon.com/python/web_scraping/monitor_a_website/
#https://www.adventuresintechland.com/detect-when-a-webpage-changes-with-python/
#https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

from pushbullet import Pushbullet
pb = Pushbullet('API_key')



# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.


# while this is true (it is true by default),
chp_number = "27"
while True:
    # set the url as VentureBeat,
    url = "http://merakiscans.com/solo-leveling/" +chp_number +"/"
    print(url)
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the manga chapter page
    response = requests.get(url, headers=headers)
    print(response)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "html.parser")

    #name_box = soup.find('ul', attrs={'class': 'lst mng_chp'})
    #name = name_box.text.strip() # strip() is used to remove starting and trailing

    checker = soup.find('div', attrs={'class': 'wpm_pag'}).find('b')
    print(checker.text.strip())
    
    push = pb.push_link("New update for chapter: " + chp_number, url)

# if the string is found
    if checker.text.strip() == "Sorry, this chapter is not available yet!":
        print('No Update yet')
        time.sleep(60*30) #check every 30min
        # continue with the script,
        continue

   
    else:
        # send notification with pushbullet,


        push = pb.push_link("New update for chapter: " + chp_number, url)
        print('I found an update')

        time.sleep(60*60*18) #sleep for 18 hours

        break
