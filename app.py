import os
from flask import Flask
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  

@app.route("/")
def home():
    return "Tambola backend is running!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
