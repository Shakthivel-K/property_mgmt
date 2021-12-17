from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__,template_folder="webpages")
@app.route("/")
def index():
    return render_template("home.html")
if __name__ == "__main__":
    app.run()


