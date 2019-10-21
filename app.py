from flask import Flask, jsonify, render_template, request
from db import *
import os
app = Flask(__name__)



# developer = os.getenv("DEVELOPER", "Me")
api_key=os.getenv("API_KEY","0")
environment=os.getenv("ENVIROMENT","development")


db = db(api_key)
db.start()
# print(db.r.hget("Joker","id").decode('utf-8'))


redis=db.r
@app.route("/")
def home():
    return render_template("index.html", redis=redis)



if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)
