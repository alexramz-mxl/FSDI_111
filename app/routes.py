from flask import Flask # From the flask module import flask class

app = Flask(__name__)   # Create an instance of Flask (now an object)

@app.get("/")           # Flask decorator that allows us to define routes
def index():            # View function
    me = {              # Python dictionary (key-value pairs)
        "first_name": "Alexis",
        "last_name": "Pastrana",
        "hobbies": "Calistenics",
        "is_online": True
    }
    return me           # Returning a dictionary in flask converts is to JSON!


