from flask import Flask
from flask import render_template
from main import *
app = Flask(__name__,template_folder='html_files')

@app.route("/")
def index():
    string=query_buffer.execute("tab","selection","select * from tab;",root_connection);
    return render_template("index.html",data=string)
@app.route("/index2")
def index2():
    string=query_buffer.execute("tab","selection","select * from tab;",root_connection);
    return render_template("index2.html",data=string)

if __name__ == "__main__":
    app.run()