from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "Family.Pizza.4??"

from webFlask import routes