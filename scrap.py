from bs4 import BeautifulSoup
import requests
from get_links import get_all_links


class Apartment:
    def __init__(self, city, price, area, house_type, rooms, bars, furniture, lift, parking, air_condition):
        self.city = city
        self.price = price
        self.area = area
        self.house_type = house_type
        self.rooms = rooms
        self.bars = bars
        self.furniture = furniture
        self.lift = lift
        self.parking = parking
        self.air_condition = air_condition

    def __str__(self):
        return str(self.city) + '\n' + str(self.price) + '\n' + str(self.area) + '\n' + str(self.house_type) + '\n' + \
               "rooms: " + str(self.rooms) + '\n' + "bars: " + str(self.bars) + ' \n' + 'furn: ' + str(self.furniture) \
               + '\n' + "lift: " + str(self.lift) + '\n' + str(self.parking) + '\n' + str(
            self.air_condition)

    def get_city(self):
        return self.city

    # return the price converted to int
    def get_price(self):
        try:
            price_int = (int(self.price.replace(',', '')))
            return price_int
        except ValueError:
            return 0

    def get_area(self):
        try:
            return int(self.area)
        except ValueError:
            return 0

    def get_house_type(self):
        return self.house_type

    def get_rooms(self):
        return self.rooms

    def get_bars(self):
        return 1 if self.bars else 0

    def get_furniture(self):
        return 1 if self.furniture else 0

    def get_lift(self):
        return 1 if self.lift else 0

    def get_parking(self):
        return self.parking

    def get_air_condition(self):
        return self.air_condition


# return the city where the house is located
def get_city(soup):
    ul_html = soup.find("ul", class_="breadcrumb")
    li_html = ul_html.find_all("a")[1]
    city_html = li_html["href"]
    city = city_html.split("$$")[0].split("=")[1]
    return city


# return the price of the house
def get_price(soup):
    price_html = soup.find("div", class_="price")
    return price_html.text.split().pop(1)


# return the area of the house in squre meters
def get_area(soup):
    balcony_html = soup.find_all("div", style="float:right; width:130px;")[3].text
    return balcony_html.split(':')[1].split('\n')[0]


# return the number of rooms in the house
def get_rooms(soup):
    rooms_html = soup.find("div", class_="right")
    rooms_text = rooms_html.find("h1").string
    return rooms_text.split(',').pop(1).split(' ').pop(1)


# return the house type ( apartment, private home, penthouse .....)
def get_house_type(soup):
    type_html = soup.find("div", class_="right")
    type_text = type_html.find("h1").string
    return type_text.split(',').pop(0)


# return if the house has bars
def has_bars(soup):
    image = soup.find_all("img", class_="itemsAd")[0]["src"]
    if image == "/Images/uncheked.png":
        return False
    elif image == "/Images/checked.png":
        return True


# return if the house has furniture
def has_furniture(soup):
    image = soup.find_all("img", class_="itemsAd")[1]["src"]
    if image == "/Images/uncheked.png":
        return False
    elif image == "/Images/checked.png":
        return True


# return if the house has lift
def has_lift(soup):
    image = soup.find_all("img", class_="itemsAd")[2]["src"]
    if image == "/Images/uncheked.png":
        return False
    elif image == "/Images/checked.png":
        return True


# return the amounts of balconies in the house
def get_balconies(soup):
    balcony_html = soup.find_all("div", style="float:right; width:130px;")[2].text
    balcony_html.split(':')[1]
    return balcony_html.split(':')[1]


# return the parking in the house
def get_parking(soup):
    parking_html = soup.find_all("div", style="float:right; width:180px;")[1].text
    return parking_html.split(':')[1]


# return the type of air condition
def get_air_condition(soup):
    air_condition = soup.find_all("div", style="float:right; width:180px;")[2].text
    return air_condition.split(':')[1]


# return all the apartments objects
def get_data():
    apartments_links = get_all_links()

    apartments = []
    for apartment_link in apartments_links:
        htmt_text = requests.get(apartment_link).text
        soup = BeautifulSoup(htmt_text, "lxml")

        try:
            city = get_city(soup)
            price = get_price(soup)
            squre_meter = get_area(soup)
            house_type = get_house_type(soup)
            rooms = get_rooms(soup)
            lift = has_lift(soup)
            furniture = has_furniture(soup)
            bars = has_bars(soup)
            parking = get_parking(soup)
            air_condition = get_air_condition(soup)
            new_apartment = Apartment(city, price, squre_meter, house_type, rooms, bars, furniture, lift,
                                      parking, air_condition)
            # print(new_apartment)
            # print(apartment_link)
            # print('\n')
            apartments.append(new_apartment)

        except :
            print("exception in link:" + apartment_link)

    return apartments
