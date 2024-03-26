from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
import os
import traceback
import random
from dotenv import load_dotenv
load_dotenv()
from flask_flatpages import FlatPages

app = Flask(__name__)
FAVICON = "./assets/favicon.png"
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'
flatpages = FlatPages(app)
import markdown
ASSETS_FOLDER = "./assets"
app.config['ASSETS_FOLDER'] = ASSETS_FOLDER

@app.route("/home")
def index_redirect():
    return redirect(url_for("index"))

@app.route("/")
def index():
    return render_template("index.html", favicon=FAVICON)

@app.route("/projects")
def projects():
    return render_template("projects.html", favicon=FAVICON)

@app.route("/blog")
def blog():
    posts = [post for post in flatpages if 'date' in post.meta]
    posts.sort(key=lambda item: item.meta['date'], reverse=True)
    return render_template('blog.html', posts=posts, favicon=FAVICON)
        


@app.route("/about")
def about():
    return render_template("about.html", favicon=FAVICON)

@app.route('/post/<path>/')
def page(path):
    page = flatpages.get_or_404(path)
    html = markdown.markdown(page.body)
    return render_template('blog-post.html', post=page, post_body=html, favicon=FAVICON)

@app.route('/assets/<filename>', methods=['GET'])
def get_api_image(filename):
    return send_from_directory(app.config['ASSETS_FOLDER'], filename)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', text="404 Not Found", favicon=FAVICON), 404

@app.errorhandler(405)
def method_not_allowed(error):
  return render_template("error.html", text="Method Not Allowed", favicon=FAVICON), 405

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8033)