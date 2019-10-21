from flask import Flask, jsonify, render_template, request
from db import *
# import requests as rq
import os
app = Flask(__name__)



# developer = os.getenv("DEVELOPER", "Me")
api_key=os.getenv("API_KEY","0")
environment=os.getenv("ENVIROMENT","development")


db = db(api_key)
db.start()


# rq.get(f"https://api.themoviedb.org/3/movie/76341?api_key={api_key}")

@app.route("/")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)
