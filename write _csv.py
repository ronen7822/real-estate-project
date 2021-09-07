import csv
import time
import scrap

head_line = ['city', 'price', 'area', 'house type', 'rooms', 'bars', 'furniture', 'lift',
             'parking', 'air condition']


# return row of data on given apartment
def get_row(apartment):
    row = [apartment.get_city(), apartment.get_price(), apartment.get_area(), apartment.get_house_type(),
           apartment.get_rooms(), apartment.get_bars(), apartment.get_furniture(), apartment.get_lift(),
           apartment.get_parking(), apartment.get_air_condition()]

    return row


# writes the apartments data to the csv file
def write_to_csv():
    apartments_data = scrap.get_data()
    
    with open('apartments.csv', "w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(head_line)
        for apartment in apartments_data:
            csv_writer.writerow(get_row(apartment))


start_time = time.time()
write_to_csv()
print(time.time() - start_time, "seconds")
