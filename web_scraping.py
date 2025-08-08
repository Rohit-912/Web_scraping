from bs4 import BeautifulSoup
import requests
import textwrap

url='https://www.thehindu.com/news/national/maharashtra/maharashtra-fda-suspends-mla-hostel-caterers-licence-after-stale-food-claim-by-legislator/article69794613.ece'
headers = {"User-Agent": "Mozilla/5.0"}

resp=requests.get(url,headers=headers)
resp.raise_for_status()

soup=BeautifulSoup(resp.text,'html.parser')
soup.prettify()

paragraphs=soup.find_all('p')

article_text = "\n".join(p.get_text(strip=True) for p in paragraphs[9:-5])
wrapped_text = textwrap.fill(article_text, width=80)

with open("scraped.txt","w") as file:
    file.write(article_text)