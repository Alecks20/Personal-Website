from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
import os
import traceback
import random
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
FAVICON = "https://cdn.a3d.pro/uploads/iawzhqbq8ssi-xxckj0k57-wh-pb493hxib-i6sojywwwr22a7uyhi-lj15xgv5pxtc3uyp7lagvfdbadmdx-j1qv98x2-w-8-jyiynxzsnnvrlx6tg-0it-q9en9p6y9p12wxpneopm9eqw8l86ef.png"


@app.route("/home")
def index():
    return render_template('error.html', text="Under Construction", favicon=FAVICON)


@app.route("/")
def index_redirect():
    return redirect(url_for("index"))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', text="404 Not Found"), 404

@app.errorhandler(405)
def method_not_allowed(error):
  return render_template("error.html", text="Method Not Allowed"), 405

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8033)