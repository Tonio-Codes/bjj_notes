from flask import Flask, request, jsonify, url_for, redirect, render_template
import notes


app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def hello_world():
    if request.method == "POST":
        return redirect(url_for("render_notes"))
    else:
        return render_template("landing.html")

@app.route("/api/<user>",defaults={"date": None})
@app.route("/api/<user>/<date>", methods=["GET"])
def get_notes(user,date):
    if request.method == "GET":
        notes = get_notes(user,date)
        return jsonify(notes)

@app.route("/notes",methods=["POST","GET"])
def render_notes():
    if request.method == "GET":
        return render_template("notes_page.html")
        




app.run(debug=True)