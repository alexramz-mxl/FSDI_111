#!/user/bin/env python3
# -*- coding utf8 -*-
"""Sample Hello World Flask APP"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello ():
    return "<h1>HELLO WORLD!</h1>"

@app.route("/products")
def products():
    products_list = ["Grapes", "Berries", "Melons"]
    bullet_list = "".join(
        "<li>%s</li>" % product for product in product_list
    )
    return "<ul>%s</ul>" % bullet_list
    