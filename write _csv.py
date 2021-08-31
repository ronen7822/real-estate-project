import csv
import time
import scrap


# writes the apartments data to the csv file
def write_to_csv():

    apartments_data = scrap.get_data()
    print("finished to gather the data")

    with open('apartments.csv', "w", newline='', encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        head_line = ['city', 'price', 'area', 'house type', 'rooms', 'bars', 'furniture', 'lift',
                     'parking', 'air condition']
        csv_writer.writerow(head_line)

        for apartment in apartments_data:
            row = []

            row.append(apartment.get_city())
            row.append(apartment.get_price())
            row.append(apartment.get_area())
            row.append(apartment.get_house_type())
            row.append(apartment.get_rooms())
            row.append(apartment.get_bars())
            row.append(apartment.get_furniture())
            row.append(apartment.get_lift())
            row.append(apartment.get_parking())
            row.append(apartment.get_air_condition())

            csv_writer.writerow(row)


start_time = time.time()
write_to_csv()
print(time.time() - start_time, "seconds")
