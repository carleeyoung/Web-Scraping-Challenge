from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars #this is the python file we created - allows us to use functions defined in this file

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    Mars_data = mongo.db.collection.find_one()
    return render_template("index.html", Mars=Mars_data)

#second page called scrape
@app.route("/scrape")
def scrape():
    Mars_data = scrape_mars.scrape()
    mongo.db.collection.update({}, Mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)