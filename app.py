from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
import os
import traceback
import random
from dotenv import load_dotenv
load_dotenv()
from flask_flatpages import FlatPages
from datetime import datetime

app = Flask(__name__)
FAVICON = "https://assets.alecks.dev/branding/favicon2.png"
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'
flatpages = FlatPages(app)
import markdown
ASSETS_FOLDER = "./assets"
app.config['ASSETS_FOLDER'] = ASSETS_FOLDER
try:
    TRACKING_ID = os.environ["TRACKING_ID"]
except:
    TRACKING_ID = " "

navigation = """
<nav class="nav-container">
 <ul class="nav">
     <i class="fas fa-home gray-icon"></i><li><a href="/">Home</a></li>
     <i class="fas fa-bookmark gray-icon"></i><li><a href="/blog">Blog</a></li>
     <i class="fas fa-boxes-stacked gray-icon"></i><li><a href="/projects">Projects</a></li>
     <i class="fas fa-address-card gray-icon"></i><li><a href="/about">About</a></li>
 </ul>
</nav>
"""

footer = """
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
    return render_template("index.html", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer,active_1=active)

@app.route("/upload")
def upload():
    return render_template("upload.html", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)

@app.route("/projects")
def projects():
    return render_template("projects.html", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)

@app.route("/status")
def status():
    return render_template("status.html", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)

@app.route("/blog")
def blog():
    posts = [post for post in flatpages if 'date' in post.meta]
    posts.sort(key=lambda item: item.meta['date'], reverse=True)
    return render_template('blog.html', posts=posts, favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)
        
@app.route("/about")
def about():
    return render_template("about.html", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)

@app.route('/post/<path>/')
def page(path):
    page = flatpages.get_or_404(path)
    html = markdown.markdown(page.body)
    return render_template('blog-post.html', post=page, post_body=html, favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', text="404 Not Found", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer), 404

@app.errorhandler(405)
def method_not_allowed(error):
  return render_template("error.html", text="Method Not Allowed", favicon=FAVICON, navigation=navigation, tracking_id=TRACKING_ID,footer=footer), 405




if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=80)