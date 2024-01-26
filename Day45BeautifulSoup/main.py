from bs4 import BeautifulSoup 
import numpy as np
import requests 

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")

all_news_headlines = soup.select(selector="span.titleline a")
all_news_links = soup.select(selector="span.titleline a")
all_news_upvotes = soup.select(selector="span.subline span.score")

print(all_news_upvotes)
# for headline in all_news_headlines:
#     print(headline.text)
article_titles = []
article_links = []
article_upvotes = []

for link in all_news_links:
    hrefValue = link.get("href")
    article_links.append(hrefValue)
    
for headline in all_news_headlines:
    titleValue = headline.getText()
    article_titles.append(titleValue)

for upvote in all_news_upvotes:
    upvoteValue = upvote.text
    upvoteValue = upvoteValue.split(" ")[0]
    print(upvoteValue)
    article_upvotes.append(upvoteValue)


article_title_with_most_upvotes = article_titles[np.argmax(article_upvotes)]
article_title_with_most_upvotes = article_links[np.argmax(article_upvotes)]

print(article_title_with_most_upvotes)

print(article_links)
print(article_titles)
print(article_upvotes)

# first_article_link = soup.select_one(selector="span.titleline a").get("href")
# # first_article_link = soup.find(name="span",class_="titleline")
# print(first_article_link)

# first_article_upvotes = soup.select_one(selector="span.score").text
# print(first_article_upvotes)


# # first_story_article_upvote = soup.find(name="span",_class="score",recursive=True)
# # print(first_story_article_upvote.text)


# print(soup.title)


# with open("website.html",encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents,"html.parser")

# print("soup.title.string",soup.title.string)
# all_paragraphs = soup.find_all(name="p")
# all_links = soup.find_all(name="a")

# for paragraph in all_paragraphs:
#     print(paragraph.string)

# for link in all_links:
#     print(link.get("href"))

# heading = soup.find(name="h1",id="name")
# print(heading.string)

# section_heading = soup.find(name="h3",class_="heading")
# print(section_heading.string)
# print(section_heading.getText())
# print(section_heading.get("class"))
# print(section_heading.name)

# company_url = soup.select_one(selector="p a") 
# print(company_url.string)

# all_headings = soup.select(selector=".heading")
# for heading in all_headings:
#     print(heading.getText())

# # print("soup.title.name",soup)
# # print("soup.title.string",soup.title.string)
