import os

from flask import Flask


app = Flask(__name__, instance_relative_config=True)



@app.route('/')
def index():
    return "<p>Index</p>"

if __name__=='__main__':
    app.run(debug=True)