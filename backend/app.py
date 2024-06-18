from flask import Flask, jsonify
from flask_cors import CORS
from readEmail import readEmail
app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods = ['GET'])
def get_data():
    test = {"name" : "saas", "number" : 1}
    emails = readEmail()

    return jsonify(emails)


if __name__ == "__main__":
    app.run(debug = True)