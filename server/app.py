import flask
from flask import Flask

version = "1.0.0"

app = Flask(__name__)

@app.route('/api/version')
def index():
    return version


if __name__ == '__main__':
    app.run(debug=True)