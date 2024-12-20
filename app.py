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

#app.config["CORS_HEADERS"] = "Content-Type"
FAVICON = "/public/static-assets/pepe-favicon.jpg"
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'
flatpages = FlatPages(app)

try:
    TRACKING_ID = os.environ["TRACKING_ID"]
except:
    TRACKING_ID = " "

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
     <a class="nav-text" href="/"><i class="fas fa-home gray-icon"></i><li>Home</a></li>
   </ul>
   <ul class="icon-container nav">
     <a class="nav-text" href="/blog"><i class="fas fa-bookmark gray-icon"></i><li>Blog</a></li>
   </ul>
   <ul class="icon-container nav">
     <a class="nav-text" href="/experience"><i class="fas fa-toolbox gray-icon"></i><li>Experience</a></li>
   </ul>
   <ul class="icon-container nav">
     <a class="nav-text" href="/projects"><i class="fas fa-boxes gray-icon"></i><li>Projects</a></li>
   </ul>
   <ul class="icon-container nav">
     <a class="nav-text" href="/about"><i class="fas fa-address-card gray-icon"></i><li>About</a></li>
   </ul>
</nav>
"""

footer = f"""
    <div class="footer">
        <p>© 2024 Alecks</p>
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
    return render_template("index.html", favicon=FAVICON, navigation=navigation, footer=footer, posts=latest_posts)

@app.route("/projects")
def projects():
    return render_template("projects.html", favicon=FAVICON, navigation=navigation, footer=footer)

@app.route("/experience")
def experience():
    return render_template("experience.html", favicon=FAVICON, navigation=navigation, footer=footer)

@app.route("/blog")
def blog():
    posts = [post for post in flatpages if 'date' in post.meta]
    posts.sort(key=lambda item: item.meta['date'], reverse=True)
    for post in posts:
        post.meta['time_ago'] = calculate_time_ago(post.meta['date']) 
    return render_template('blog.html', posts=posts, favicon=FAVICON, navigation=navigation, footer=footer)
        
@app.route("/about")
def about():
    return render_template("about.html", favicon=FAVICON, navigation=navigation, footer=footer)

@app.route("/passgen")
def passgen():
    return render_template("passgen.html",favicon=FAVICON, navigation=navigation, footer=footer)

@app.route('/post/<path>/')
def page(path):
    page = flatpages.get_or_404(path)
    page.meta['time_ago'] = calculate_time_ago(page.meta['date']) 
    html = markdown.markdown(page.body)
    return render_template('blog-post.html', post=page, post_body=html, favicon=FAVICON, navigation=navigation, footer=footer)

#Serving static content
@app.route('/public/static-assets/<filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory("./assets/", filename)

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
    app.run(host="0.0.0.0",debug=True,port=80)
