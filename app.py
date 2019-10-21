from flask import Flask, jsonify, render_template, request
from db import *
import os
app = Flask(__name__)



developer = os.getenv("DEVELOPER", "Me")
api_key=os.getenv("API_KEY","0")
environment=os.getenv("ENVIROMENT","development")


db = db(api_key)
db.start()
# print(db.r.hget("Joker","id").decode('utf-8'))


redis_server=db.redis_server
@app.route("/")
def home():
    return render_template("index.html", redis_server=redis_server)



if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)
