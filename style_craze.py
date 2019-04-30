import requests
import csv
from bs4 import BeautifulSoup
# pages[] contains the url of all pages
# blog_links[] contains the articles in each page from pages[]

# f = csv.writer(open('z-artist-names.csv', 'w'))
# f.writerow(['Name', 'Link'])



# for i in range(1, 5):
url = 'https://www.stylecraze.com/articles/skin/'
    # pages.append(url)


# for item in pages:
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

title = soup.find_all(class_='posttitle')
    # last_links.decompose()
# print(title)
# extracted_title_content = title[0].contents[0]
# print(title[0])
# print(extracted_title_content)
blog_links = []
pages = []
pages.append(url) # Appending the initial url as it is different from others.

for i in range(1,5) :
    url = 'https://www.stylecraze.com/articles/skin/page/' + str(i)+'/'
    pages.append(url)
print(pages)
for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    h1_tag_list = soup.find_all(class_='posttitle')
    flag = 0
    for html_content in h1_tag_list:
        if flag == 0: # For the large post
            extracted_title_content = html_content.contents
            exact_article_link_a_tag = extracted_title_content[0]
            output = exact_article_link_a_tag['href']
            # print(output + "\n")
            blog_links.append(output)
            flag=1
        else: # For rest of the posts
            extracted_title_content = html_content.contents
            exact_article_link_a_tag = extracted_title_content[1]
            output = exact_article_link_a_tag['href']
            blog_links.append(output)
            # print(output + "\n")
print(blog_links)


for item in blog_links:
    # From each blog link, extracting the blog details
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Extracting Author Name
    author_name = soup.find('div',attrs={"class":"pullauthor-details"}).find('a').text
    print(author_name)

    # Extracting Content
    content = soup.find('div',attrs={"class":"entry-content"}).find('p')
    print(content.find('p').text)

    # Extracting Images
    image = soup.find('img',attrs={"class":"wp-post-image"})
    output = image['src']
    print(output)

    # Extracting the time
    time = soup.find('time')
    output =time.text
    print(output)

    #Extracting the Blog link


# p_tags = soup.findAll('')
# print(p_tags)
# for x in content:
    # print(x)
    # flag = 0
    # for t in title:
    #     if flag == 0:
    #         extracted_title_content = t.contents
    #         ext = extracted_title_content[0]
    #         output = ext['href']
    #         print(output + "\n")
    #         blog_links.append(output)
    #         flag=1
    #     else:
    #         extracted_title_content = t.contents
    #         ext = extracted_title_content[1]
    #         output = ext['href']
    #         blog_links.append(output)
    #         print(output + "\n")
    # artist_name_list = soup.find(class_='BodyText')
    # artist_name_list_items = artist_name_list.find_all('a')

    # for artist_name in artist_name_list_items:
    #     names = artist_name.contents[0]
    #     links = 'https://web.archive.org' + artist_name.get('href')

    #     f.writerow([names, links])
