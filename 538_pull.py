import requests
import bs4

r =requests.get('https://projects.fivethirtyeight.com/2017-nfl-predictions/')
r.raise_for_status()
rsoup = bs4.BeautifulSoup(r.text)
print('done')