from flask import Flask, render_template

from constants import *
from login.login import login_blueprint, login_manager

app = Flask(
    __name__.split('.')[0],
    template_folder=str(TEMPLATE_DIR),
    static_folder=str(STATIC_DIR)
)
app.register_blueprint(login_blueprint)
app.config.from_pyfile(str(SRC_DIR/"config.py"))
app.secret_key = app.config.get("SECRET_KEY")

login_manager.init_app(app)

@app.route('/')
def index():
    return render_template("layout.html.jinja")

if __name__ == '__main__':
    app.run()