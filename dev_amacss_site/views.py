from dev_amacss_site import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html",
        title="AMACSS Development Site"
    )
