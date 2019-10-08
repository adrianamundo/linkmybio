from flask import Flask, render_template
from datetime import datetime
import yaml, os

app = Flask(__name__)

info = yaml.load(open('links.yaml'))
environment=os.getenv("ENVIRONMENT","development")


@app.route("/")
def about():
    links = info['links']
    return render_template("index.html", links = links)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    #print("Local change")
    app.run(host="0.0.0.0",debug=debug)