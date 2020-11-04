#scrape nytimes homepage for featured titles & headlines
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.nytimes.com")
soup = BeautifulSoup(page.content, 'html.parser')

titles = soup.find_all(['h2', 'h3']) #soup.find_all(class_='css-kej3w4')
for titl in titles:
	print(titl.get_text())