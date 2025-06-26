from router import route
from utils import render_template
import os
from config import FILE_DIR

@route("/")
def homepage(request):
    return 200, "text/html", "<h1>Hello World</h1>"

@route("/files/")
def list_files(request):


    try:
        files = os.listdir(FILE_DIR)
        html = "<h1>Files in server</h1><ul>"
        for f in files:
            html += f"<li><a href='/files/" + f + "'>" + f + "</a></li>"
        html += "</ul>"
        return 200, "text/html", html
    except FileNotFoundError:
        return 500, "text/plain", "Directory not found"

@route("/home")
def home_page(request):
    html = render_template("home.html")
    return 200,"text/html",html

from router import ROUTES  # ✅ import ROUTES explicitly

print("Routes registered:", list(ROUTES.keys()))
