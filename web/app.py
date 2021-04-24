"""
Theo's Flask API.
"""

from flask import Flask
from flask import render_template
from flask import abort
import os

app = Flask(__name__)

STATUS_OK = "HTTP/1.0 200 OK\n\n"
STATUS_FORBIDDEN = "HTTP/1.0 403 Forbidden\n\n"
STATUS_NOT_FOUND = "HTTP/1.0 404 Not Found\n\n"


@app.route("/<fname>")
def hello(fname):

    if "//" in fname or "~" in fname or ".." in fname:
        abort(403)

    source_path = "templates/" + fname
    if os.path.isfile(source_path):
        return render_template(fname)
    else:
        abort(404)



@app.errorhandler(404)
def notfound(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"),403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
