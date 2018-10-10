from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/members')
def members():
    return "Matthew, Nonthicha, Phumarin"

#export FLASK_APP=path
#flask run