from flask import Flask, render_template, url_for

from constants import *
from login.index import login_page

app = Flask(
    __name__.split('.')[0],
    template_folder = str(TEMPLATE_DIR)
)
app.register_blueprint(login_page, url_prefix='/login/')
app.static_folder = str(STATIC_DIR)

@app.route('/')
def root():
    return render_template("layout.html.jinja")

if __name__ == '__main__':
    app.run()