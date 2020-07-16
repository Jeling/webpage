from flask import render_template
from flask import request, redirect
from flask import Flask

app = Flask(__name__)

@app.route("/o-mnie")
def o_mnie():
    return render_template("o-mnie.html")

@app.route("/kontakt", methods=['GET', 'POST'])
def kontakt():
    if request.method == 'GET':
        print("We received GET")
        return render_template("kontakt.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/kontakt")