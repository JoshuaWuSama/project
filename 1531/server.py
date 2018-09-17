from flask import Flask
user_input = []
app = Flask(__name__)
app.config["SECRET_KEY"] = "Highly secret key"
