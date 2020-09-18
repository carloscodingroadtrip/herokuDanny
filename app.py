from flask import Flask, jsonify, render_template

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"<h4>Available Routes:</h4>"
        f'<a href="/api/v1.0/ids">/api/v1.0/ids</a><br/>'
        f'<a href="/api/v1.0/info/1286">/api/v1.0/info/subject_id</a><br/>'
        f'<a href="/api/v1.0/subjects">/api/v1.0/subjects</a><br/>'
        f'<a href="/api/v1.0/subjects/1286">/api/v1.0/subjects/subject_id</a><br/>'
        f'<a href="/"><h4>Back</h4></a><br/>'
    )
