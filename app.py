from flask import Flask, jsonify
import os

#Init app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({ 'msg' : 'Hello World!' })

#Run Server
if __name__ == "__main__":
    app.run(debug=True)