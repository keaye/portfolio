from flask import Flask, render_template, abort

app = Flask(__name__)



projects = [
    {
        "name": "Blog-entry",
        "thumb": "img/blog.jpg",
        "hero": "img/blog-hero.jpg",
        "categories": ["flask", "python"],
        "slug": "blog-page",
        "prod": "https://blog-icg3.onrender.com",
    },
    {
        "name": "FizzBuzz",
        "thumb": "img/fizzbuzz.jpg",
        "hero": "img/fizz-hero.png",
        "categories": ["flask", "python"],
        "slug": "fizz-buzz",
        "prod": "https://testss-rosy.vercel.app/"
    },
    {
        "name": " Habit-tracker",
        "thumb": "img/tracker.jpg",
        "hero": "img/tracker-hero.png",
        "categories": ["flask", "python"],
        "slug": "habit-tracker",
        "prod": "https://habit-i6s1.onrender.com"
    },
    {
        "name": "Watchlist",
        "thumb": "img/watchlist.jpg",
        "hero": "img/watchlist-hero.png",
        "categories": ["flask", "python"],
        "slug": "movie-watchlist",
        "prod": "https://movie-watchlist-hlxf.onrender.com"
    },
     {
        "name": "Weather-App",
        "thumb": "img/weather.jpg",
        "hero": "img/weather-hero.png",
        "categories": ["flask", "python"],
        "slug": "weather-app",
        "prod": "https://weather-app-tlvj.onrender.com"
    },
]

slug_to_project = {project["slug"]: project for project in projects}



@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])






@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404