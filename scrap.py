# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)

# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.

# while this is true (it is true by default),
chp_number = 27
while True:
    # set the url as VentureBeat,
    url = "http://merakiscans.com/solo-leveling/" +chp_number +"/"
    print(url)
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    print(response)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "html.parser")

    #name_box = soup.find('ul', attrs={'class': 'lst mng_chp'})
    #name = name_box.text.strip() # strip() is used to remove starting and trailing
    #print name
    #bol = False



    # if the number of times the word "Google" occurs on the page is less than 1,
    if str(soup).find("Sorry, this chapter is not available yet!") == -1:
        print('No Update yet')
        # wait 60 seconds,
        time.sleep(60)
        # continue with the script,
        continue

    # but if the word "Google" occurs any other number of times,
    else:
        # create an email message with just a subject line,

        print('I found something')


        # send the email
        # server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        # server.quit()

        break
