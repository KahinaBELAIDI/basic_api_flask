# import statements
from flask import Flask, request, Response, jsonify, make_response, render_template
from datetime import datetime
import re
from flask_swagger_ui import get_swaggerui_blueprint
from db import create_tables, connect_to_db
import controller
import csv
import numpy as np
import base64
from PIL import Image
from io import StringIO


app = Flask(__name__)
db = connect_to_db()

# API Routes


@app.route("/")  # route to test api accessibility
def home():
    return "Hello, Kahina! "


@app.route("/images", methods=["POST"])
def resizeImage1():
    print("**** Here in resize image endpoint ****")
    newImage = request.get_json()
    image_name = newImage["name"]
    depth = newImage["depth"]
    result = controller.insert_image(image_name, depth, '', '')
    return jsonify(result)


@ app.route("/images/<id>", methods=["GET"])
def getImage(id):
    print("**** Here in get image endpoint ****")
    result = controller.get_by_id(id)
    print("hhhd")
    return jsonify(result)


# API Doc with Swagger using blueprint
SWAGGER_URL = '/swagger'  # docs route
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Challenge 2 - Resize images"
    }


)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


# handle not found routes, send as respons status 404 / page not found


@ app.errorhandler(404)
def page_not_found(e):

    # Message to the user
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation."
            }
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == "__main__":
    create_tables()
    app.run(host='127.0.0.1', port=5000, debug=False)
