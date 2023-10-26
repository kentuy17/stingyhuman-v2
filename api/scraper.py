import requests
from bs4 import BeautifulSoup
import json

URL = "https://bestreviews.com"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
all_categories = soup.find("li", class_="all-categories")

# categories_soup = BeautifulSoup(all_categories, "html.parser")
# extracted = soup.find_all("a")
a_links = all_categories.find_all('a', attrs={'href': True})
# extracted = a_links.a['href']

links = []
for tag in a_links:
  # new_tag = BeautifulSoup(tag, 'html.parser')
  links.append(URL + tag['href'])
  # print(tag['href'])

dictionary = {
  "categories": links
}

# Serializing json
categories_obj = json.dumps(dictionary, indent=2)
 
# Writing to sample.json
with open("categories.json", "w") as outfile:
  outfile.write(categories_obj)

# print(dictionary)