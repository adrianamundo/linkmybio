from flask import Flask, render_template, url_for
from datetime import datetime
import yaml, os

app = Flask(__name__)

info = yaml.load(open('links.yaml'))
environment=os.getenv("ENVIRONMENT","development")


@app.route("/")
def about():
    images ={"profile" : url_for('static', filename = 'images/profille.jpeg'),}
    links = info['links']
    date = datetime.now()
    date = str(date)
    return render_template("index.html", links = links, info=info, images = images, date = date)
      
if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    #print("Local change")
    app.run(host="0.0.0.0",debug=debug)