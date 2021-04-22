from requests import get
from rest import weather_data
from flask import Flask, render_template
from flask.globals import request

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/project")
def project():
    return render_template("project.html")


@app.route("/location", methods=['GET'])
def location():
    x = request.args.get("x")
    r = get(
        "https://www.weather-forecast.com/locations/"+x+"/forecasts/latest")

    if r.status_code != 200:
        return render_template("notfound.html")

    args = weather_data(x)
    return render_template("location.html", data=args)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
