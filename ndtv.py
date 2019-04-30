import requests
import csv
from bs4 import BeautifulSoup

url = 'https://food.ndtv.com/health'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

blog_links = []

# Extracting Blog Links

ti = soup.findAll('h2')
for t in ti:
    html_contents = t.contents
    first_ele = html_contents[0]
    exact_link = first_ele['href']
    blog_links.append(exact_link)


# print(blog_links)
#Extrating Info from each blog link

for link in blog_links:
    url = str(link)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    #Extracting Image
    pic = soup.find('picture')
    print(pic.contents[1]['src'])
    
    #Extracting Title
    tit = soup.find('h1')
    print(tit.text)
    #Extracting Author
    auth = soup.find('p',attrs={"class":"article-dtl-desc"})
    print(auth.contents[0].strip().strip("|"))
    
    #Extracting Time
    time = soup.find('p',attrs={"class":"article-dtl-desc"})
    print(time.contents[1].text)
    #Extracting Content
    vars = 0