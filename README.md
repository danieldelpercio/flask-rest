# flask-rest
An app to experiment with a REST API in flask.

To run:
## CMD
```
set FLASK_APP=flask-rest
flask run
```
## bash
```
export FLASK_APP=flask-rest
flask run
```
# Product CRUD
This CRUD is based on a tutorial. It is here for reference purposes.
The API is:
 - GET: /products - to get all the products
 - POST: /products - add a product
 - PUT: /products/\<id> - to modify a product
 - DELETE: /products/\<id> - to delete a product
 
 Product looks like:
 ```
      {
        "id": number,
        "name": "name",
        "description": "description"
    }
 ```
# Weather API
This API is for managing cities and their weather.
The API has:
 - POST: /city - pass a city name to add it to the database and populate it's data from POST /weather
 - POST: /weather - pass a city name to update a city's data with the current weather data pulled from openweather API
 - GET: /weather - get all cities and their weather data
 - GET: /weather/\<id> - get the weather of a city with the chosen ID
 - PUT: /weather/\<id> - update the weather data of a city with the chosen ID
 - DELETE: /weather/\<id> - delete the weather data of the chosen ID

Weather looks like:
```
{
    "coord_lan": null,
    "coord_lon": null,
    "description": "clear sky",
    "icon": null,
    "id": 4,
    "name": "New Haven",
    "temp": 16.62
}
```
