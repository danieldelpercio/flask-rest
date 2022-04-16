import os

from flask import Flask,jsonify,request


from flaskrest import app,db,ma


#Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(200))

    def __init__(self, name, description):
        self.name = name
        self.description = description

#product schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','description')

#init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


#Create a Product
@app.route('/product',methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']

    new_product = Product(name,description)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

#Get all Products
@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

#Get a Product
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

#Update a Product
@app.route('/product/<id>',methods=['PUT'])
def update_product(id):

    product = Product.query.get(id)
    name = request.json['name']
    description = request.json['description']

    product.name = name
    product.description = description

    db.session.commit()

    return product_schema.jsonify(product)


#Delete a Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)


