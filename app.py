#FLASK
from flask import Flask, jsonify, render_template, request
import requests as rq
app = Flask(__name__)
import os,optparse
# import yaml

# developer = os.getenv("DEVELOPER", "Me")
api_key=os.getenv("API_KEY","0")
environment=os.getenv("ENVIROMENT","development")


# with open("links.yml", 'r') as stream:
#     try:
#         data = yaml.safe_load(stream)
#     except yaml.YAMLError as exc:
#         print(exc)

rq.get(f"https://api.themoviedb.org/3/movie/76341?api_key={api_key}")

@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/academic-info")
# def academic_info():
#     return render_template("acedemic-info.html", data=data)


# @app.route("/labor-experience")
# def labor_xp():
#     return render_template("labor-experience.html", data=data)




if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)
