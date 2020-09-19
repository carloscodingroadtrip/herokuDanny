from flask import Flask, jsonify, render_template

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.static_folder = 'static'


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return render_template("index.html")
