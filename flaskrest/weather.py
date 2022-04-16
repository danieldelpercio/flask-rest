import requests

from flask import jsonify, request


from flaskrest import app, db, ma


# Weather Class/Model
class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(200))
    temp = db.Column(db.Float)
    coord_lon = db.Column(db.Float)
    coord_lan = db.Column(db.Float)
    icon = db.Column(db.String(10))

    def __init__(self, name):
        self.name = name


# Weather schema
class WeatherSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'temp',
            'coord_lon',
            'coord_lan',
            'icon'
            )


# init schema
weather_schema = WeatherSchema()
weathers_schema = WeatherSchema(many=True)


# Add a city
@app.route('/city', methods=['POST'])
def add_city():
    name = request.json['name']

    new_city = Weather(name)

    db.session.add(new_city)
    db.session.commit()

    update_weather_data()

    return weather_schema.jsonify(new_city)


# update weather data from API
@app.route('/weather', methods=['POST'])
def update_weather_data():
    city = request.json['name']

    url = ("https://api.openweathermap.org"
           "/data/2.5/weather?q={}&units=metric"
           "&appid=1dbaf7baf220c461d9be1a59aebba09a"
           )

    r = requests.get(url.format(city)).json()

    print(r)

    new_weather = Weather.query.filter_by(name=city).first()
    new_weather.name = city
    new_weather.temp = r['main']['temp']
    new_weather.description = r['weather'][0]['description']
    db.session.commit()

    return weather_schema.jsonify(new_weather)


# Get all weather data
@app.route('/weather', methods=['GET'])
def get_weathers():
    all_weathers = Weather.query.all()
    result = weathers_schema.dump(all_weathers)
    return jsonify(result)


# Get weather data for specific id
@app.route('/weather/<id>', methods=['GET'])
def get_weather(id):
    weather = Weather.query.get(id)
    return weather_schema.jsonify(weather)


# Update a Weather
@app.route('/weather/<id>', methods=['PUT'])
def update_weather(id):

    weather = Weather.query.get(id)
    name = request.json['name']
    description = request.json['description']
    temp = request.json['temp']
    coord_lan = request.json['coord_lan']
    coord_lon = request.json['coord_lon']
    icon = request.json['icon']

    weather.name = name
    weather.description = description
    weather.temp = temp
    weather.coord_lan = coord_lan
    weather.coord_lon = coord_lon
    weather.icon = icon

    db.session.commit()

    return weather_schema.jsonify(weather)


# Delete a Weather
@app.route('/weather/<id>', methods=['DELETE'])
def delete_weather(id):
    weather = Weather.query.get(id)
    db.session.delete(weather)
    db.session.commit()
    return weather_schema.jsonify(weather)
