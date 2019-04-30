import requests
import csv
from bs4 import BeautifulSoup


# f = csv.writer(open('z-artist-names.csv', 'w'))
# f.writerow(['Name', 'Link'])



# for i in range(1, 5):
url = 'https://www.goodreads.com/quotes/tag/inspirational'
    # pages.append(url)


# for item in pages:
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

authors_tags = soup.findAll('span',attrs={"class":"authorOrTitle"})
# print(title)
author_names = []
for i in authors_tags:
    author_names.append(i.text)
final_author_names = []
for i in author_names:
    # print(i.strip("\n"))
    final_author_names.append(i.replace('\n',' ').strip())
    
print(final_author_names)

authors_quotes_tags = soup.findAll('div',attrs={"class":"quoteText"})
print(authors_quotes_tags)
# author_quotes = []
# for i in authors_quotes_tags:
#     author_quotes.append(i.text)
# final_author_quotes = []
# for i in author_quotes:
#     # print(i.strip("\n"))
#     final_author_quotes.append(i.replace('\n',' ').strip())
    
# print(final_author_quotes)