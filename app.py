from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
from werkzeug.exceptions import UnprocessableEntity, HTTPException
import os
import random
from flask_flatpages import FlatPages
from datetime import datetime, timedelta
from flask_cors import CORS, cross_origin
import markdown


app = Flask(__name__)
cors = CORS(app)

app.config["CORS_HEADERS"] = "Content-Type"
FAVICON = "/content/favicon.gif"
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'
flatpages = FlatPages(app)



try:
    TRACKING_ID = os.environ["TRACKING_ID"]
except:
    TRACKING_ID = " "

MAX_ALLOWED_PASSWORD_LENGTH = 256
ALLOWED_STRING_LETTERS: list[str] = [character for character in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*"]

current_year = datetime.now().year

def calculate_time_ago(date):
    current_date = datetime.now().date()
    difference = current_date - date
    days = difference.days
    months = days // 30
    years = days // 365
    if years > 0:
        if years == 1:
            return "1 year ago"
        else:
            return f"{years} years ago"
    elif months > 0:
        if months == 1:
            return "1 month ago"
        else:
            return f"{months} months ago"
    elif days > 0:
        if days == 1:
            return "1 day ago"
        else:
            return f"{days} days ago"
    else:
        return "Today"
        
navigation = """
<nav class="nav-container">
   <ul class="icon-container nav">
     <i class="fas fa-home gray-icon"></i><li><a class="nav-text" href="/">Home</a></li>
   </ul>
   <ul class="icon-container nav">
     <i class="fas fa-bookmark gray-icon"></i><li><a class="nav-text" href="/blog">Blog</a></li>
   </ul>
   <ul class="icon-container nav">
     <i class="fas fa-screwdriver-wrench gray-icon"></i><li><a class="nav-text" href="/experience">Experience</a></li>
   </ul>
   <ul class="icon-container nav">
     <i class="fas fa-key gray-icon"></i><li><a class="nav-text" href="/passgen">Passgen</a></li>
   </ul>
   <ul class="icon-container nav">
     <i class="fas fa-address-card gray-icon"></i><li><a class="nav-text" href="/about">About</a></li>
   </ul>
</nav>
"""

footer = f"""
    <div class="footer">
        <p> © 2024 Alecks</p>
    </div>
"""

@app.route("/home")
def index_redirect():
    return redirect(url_for("index"))

@app.route("/about-me")
def about_redirect():
    return redirect(url_for("about"))

active = "active"

@app.route("/")
def index():
    posts = [post for post in flatpages if 'date' in post.meta]
    posts.sort(key=lambda item: item.meta['date'], reverse=True)
    latest_posts = posts[:3]
    for post in latest_posts:
        post.meta['time_ago'] = calculate_time_ago(post.meta['date']) 
    return render_template("index.html", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer,posts=latest_posts)

@app.route("/upload")
def upload():
    return render_template("upload.html", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)

@app.route("/experience")
def projects():
    return render_template("experience.html", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)

@app.route("/status")
def status():
    return render_template("status.html", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)

@app.route("/blog")
def blog():
    posts = [post for post in flatpages if 'date' in post.meta]
    posts.sort(key=lambda item: item.meta['date'], reverse=True)
    for post in posts:
        post.meta['time_ago'] = calculate_time_ago(post.meta['date']) 
    return render_template('blog.html', posts=posts, favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)
        
@app.route("/about")
def about():
    return render_template("about.html", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)

@app.route("/passgen")
def passgen():
    return render_template("passgen.html",favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)

@app.route('/post/<path>/')
def page(path):
    page = flatpages.get_or_404(path)
    page.meta['time_ago'] = calculate_time_ago(page.meta['date']) 
    html = markdown.markdown(page.body)
    return render_template('blog-post.html', post=page, post_body=html, favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)

def get_random_string(length: int) -> str:
    """Generates a securely random string with the length provided"""
    return "".join(map(str, [ALLOWED_STRING_LETTERS[get_random_string_index()] for _ in range(length)]))

def get_random_string_index() -> int:
    """Generates a securely random integer ranging from 0 (the beginning of the ALLOWED_STRING_LETTERS list) to the end of the ALLOWED_STRING_LETTERS list"""
    return random.SystemRandom().randint(0, len(ALLOWED_STRING_LETTERS) - 1)

@app.route("/api/generate_password/<int:password_length>")
@cross_origin()
def generate_password(password_length: int):
    if (password_length > MAX_ALLOWED_PASSWORD_LENGTH or password_length < 1):
        raise UnprocessableEntity(HTTPException(HTTPException(description=f"password_length should be an integer ranging from 1 - {MAX_ALLOWED_PASSWORD_LENGTH}, got {password_length} instead.")))
    return {"secure_password": get_random_string(password_length)}

#Serving static content
@app.route('/content/<filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory("./content/", filename)



#Error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', text="404 Not Found", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer), 404

@app.errorhandler(405)
def method_not_allowed(error):
  return render_template("error.html", text="Method Not Allowed", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer), 405

@app.errorhandler(422)
def unprocessable_entity(error):
    return render_template("error.html", text="422 Unprocessable Request", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer), 422


# Running the app (Development)
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8080)
