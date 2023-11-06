import requests
from bs4 import BeautifulSoup
import json


def topic_names(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # get all the links
    links = soup.find("div", class_="topic-name")

    if not links:
        return
    else:
        a_links = links.find_all("a", attrs={"href": True})

    print(a_links)
    # get all the names
    names = []
    # for link in a_links:
    #     names.append(link.text)

    return names


URL = "https://bestreviews.com"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
all_categories = soup.find("li", class_="all-categories")

a_links = all_categories.find_all("a", attrs={"href": True})

links = []
for tag in a_links:
    category_name = tag["href"]
    category_url = URL + tag["href"]

    # scrape sub-categories
    sub_page = requests.get(category_url)
    sub = BeautifulSoup(sub_page.content, "html.parser")
    all_sub_subcategories = sub.find("div", class_="subcategories")

    if not all_sub_subcategories:
        continue
    else:
        a_sub_links = all_sub_subcategories.find_all("a", attrs={"href": True})

    sub_categories = []
    for sub_tag in a_sub_links:
        sub_tag_link = "" + sub_tag["href"]
        sub_categories.append(sub_tag_link)

        valid_link = sub_tag_link.split("//", 1)[1]
        if sub_tag["href"] == "//bestreviews.com/apparel/bathrobes-pajamas":
            topic_names(sub_tag["href"])
            exit

    category_obj = {
        "name": category_name.split("/", 1)[1],
        "link": category_url,
        "subcategories": sub_categories,
    }
    links.append(category_obj)

    #

# Serializing json
categories_obj = json.dumps(links, indent=2)

# Writing to sample.json
with open("products.json", "w") as outfile:
    outfile.write(categories_obj)
