import pandas as pd
import pickle
from sklearn import preprocessing

df_popular_cities = pd.read_csv("cleaned data frame.csv", sep='\t')


def load_model():
    with open('./predicting model.pickle', 'rb') as file:
        model = pickle.load(file)
    return model


def make_city_encoder():
    twenty_most_popular_cities = df_popular_cities['city'].value_counts().index.tolist()[0:20]
    cities_encoder = preprocessing.LabelEncoder()
    cities_encoder.fit(twenty_most_popular_cities)
    return cities_encoder


def make_house_encoder():
    hosue_types = df_popular_cities['house type'].value_counts().index.tolist()[0:20]
    house_types_encoder = preprocessing.LabelEncoder()
    house_types_encoder.fit(hosue_types)
    return house_types_encoder


def make_neighborhood_encoder():
    neighborhoods = df_popular_cities['neighborhood']
    neighborhood_encoder = preprocessing.LabelEncoder()
    neighborhood_encoder.fit(neighborhoods)
    return neighborhood_encoder


def get_house_types():
    return df_popular_cities['house type'].value_counts().index.tolist()[0:20]


def get_cities():
    return df_popular_cities['city'].value_counts().index.tolist()[0:20]


def get_neighborhoods():
    return df_popular_cities['neighborhood'].value_counts().index.tolist()[0:350]


def predict_price(features, model, cities_encoder, house_types_encoder, neighborhood_encoder):
    x = pd.np.empty(17, dtype=object)
    x[0] = features[3]  # house_area
    x[1] = features[4]  # garden_area
    x[2] = features[5]  # rooms
    x[3] = features[6]  # balconies
    x[4] = features[7]  # air_condition
    x[5] = features[8]  # parking
    x[6] = features[9]  # protected_room
    x[7] = features[10]  # elevator
    x[8] = features[11]  # sun_balcony
    x[9] = features[12]  # renovated
    x[10] = features[13]  # furniture
    x[11] = features[14]  # accessibility
    x[12] = features[15]  # bars
    x[13] = features[16]  # storage
    x[14] = neighborhood_encoder.transform([features[1]])[0]  # neighborhood_number
    x[15] = house_types_encoder.transform([features[2]])[0]  # house type number
    x[16] = cities_encoder.transform([features[0]])[0]  # city number

    prediction = model.predict([x])[0]
    return round(prediction, 2)


# print(get_neighborhoods_in_city("Lod"))
# print(get_cities())
# print(get_house_types())
