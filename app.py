from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
import os
import traceback
import random
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/home")
def index():
    return render_template('error.html', text="Under Construction")


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