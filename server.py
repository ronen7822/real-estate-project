from flask import Flask, request, jsonify
import util
app = Flask(__name__)

model = util.load_model()
cities_encoder = util.make_city_encoder()
house_types_encoder = util.make_house_encoder()
neighborhood_encoder = util.make_neighborhood_encoder()


@app.route("/")
def hello():
    return "hello word"


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    cities = util.get_cities()
    response = jsonify({'locations': cities})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_house_types', methods=['GET'])
def get_house_types():
    home_types = util.get_house_types()
    response = jsonify({'types': home_types})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_neighborhoods', methods=['GET'])
def get_neighborhoods():
    neighborhoods = util.get_neighborhoods()
    response = jsonify({'locations': neighborhoods})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    city = request.form['city']
    neighborhood = request.form['neighborhood']
    house_type = request.form['houseType']
    house_area = float(request.form['houseArea'])
    garden_area = float(request.form['gardenArea'])
    rooms = float(request.form['rooms'])
    balconies = float(request.form['balconies'])
    air_condition = float(request.form['airCondition'])
    parking = float(request.form['parking'])
    protected_room = float(request.form['protectedRoom'])
    elevator = float(request.form['elevator'])
    sun_balcony = float(request.form['sunBalcony'])
    renovated = float(request.form['renovated'])
    furniture = float(request.form['furniture'])
    accessibility = float(request.form['accessibility'])
    bars = float(request.form['bars'])
    storage = float(request.form['storage'])

    features = [city, neighborhood, house_type, house_area, garden_area, rooms, balconies, air_condition, parking,
                protected_room, elevator, sun_balcony, renovated, furniture, accessibility, bars, storage]

    response = jsonify({
         'estimated_price':  util.predict_price(features, model, cities_encoder, house_types_encoder,
                                                neighborhood_encoder)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    print("start")
    app.run()
