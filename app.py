from flask import Flask

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Tambola backend is running!"

if __name__ == "__main__":
    app.run()
