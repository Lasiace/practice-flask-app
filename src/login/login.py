from flask import Blueprint, render_template, url_for, request, redirect, abort
from flask_login import LoginManager, current_user, login_user, logout_user

from constants import *
from login.user import User
from utils.url import redirect_on_complete

login_blueprint = Blueprint(
    'login',
    __name__.split('.')[0],
    template_folder = str(TEMPLATE_DIR / "login")
)
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    user_info = DB.find_user_info(user_id = user_id)
    return User(user_info['id'], user_info['name'])

def validateUser(username, password):
    return DB.check_user_pw(username, password)

@login_blueprint.route('/login', methods=["GET", "POST"])
def login():
    if validateUser(request.form["username"], request.form["password"]):
        user_info = DB.find_user_info(username = request.form["username"])
        user = User(user_info['id'], user_info['name'])
        login_user(user)

        return redirect_on_complete(request.args.get("on_complete"))
    return redirect(url_for("index"))

@login_blueprint.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect_on_complete(request.args.get("on_complete"))
