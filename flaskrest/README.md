# flask-rest
An app to experiment with a REST API in flask.


# Product CRUD
This CRUD is based on a tutorial. It is here for reference purposes.
The API is:
 - GET: /products to get all the products
 - POST: /products add a product
 - PUT: /products/\<id> to modify a product
 - DELETE: /products/\<id> to delete a product
 
 Product looks like:
 ```
      {
        "id": number,
        "name": "name",
        "description": "description"
    }
 ```
