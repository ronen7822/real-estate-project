from bs4 import BeautifulSoup
import requests


# return the apartment id from html element
def get_apartment_id(apartment):
    id_text = apartment['id']
    return id_text.split('_').pop(1)


# constructs new apartment link from the apartments id
def make_link(id):
    return "https://www.homeless.co.il/Sale/viewad," + id + ".aspx"


# return all the apartments links from specific page in the website
def get_apartments_links(page_link="https://www.homeless.co.il/sale/1500"):
    htmt_text = requests.get(page_link).text
    soup = BeautifulSoup(htmt_text, "lxml")
    not_brokerage = soup.find("div", id="display_table")

    apartments = not_brokerage.find_all('tr', type="ad")

    apartments_links = []
    for apartment in apartments:
        id = get_apartment_id(apartment)
        new_link = make_link(id)
        apartments_links.append(new_link)

    return apartments_links


# goes to the specified number page
def go_to_page(page_number):
    return "https://www.homeless.co.il/sale/" + str(page_number)


# return all the apartments links in the website
def get_all_links():
    all_links = []
    for i in range(0, 160):
        links_on_page = get_apartments_links(go_to_page(i))
        all_links = all_links + links_on_page
    return all_links
