from flask import Flask, render_template, abort

app = Flask(__name__)



projects = [

      {
        "name": "Weather-App",
        "thumb": "img/weather.jpg",
        "hero": "img/weather-hero.png",
        "categories": ["flask", "python"],
        "slug": "weather-app",
        "prod": "https://scour-one.vercel.app/"
    },

    {
        "name": "Blog-App",
        "thumb": "img/blog.jpg",
        "hero": "img/blog-hero.png",
        "categories": ["flask", "python"],
        "slug": "blog-app",
        "prod": "https://keay-s-blog.onrender.com"
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