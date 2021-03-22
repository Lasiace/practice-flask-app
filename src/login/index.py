from flask import Blueprint, render_template, request

from constants import *

login_page = Blueprint(
    'login',
    __name__.split('.')[0],
    template_folder = str(TEMPLATE_DIR / "login")
)

@login_page.route('/')
def index():
    return render_template('login/index.html.jinja', l=range(1,4))

@login_page.route('/', methods=["POST", "GET"])
def authenticate():
    if request.method == "POST":
        return "got it"
    return "nop"
