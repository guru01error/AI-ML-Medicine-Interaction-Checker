from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "AI Medicine Checker is running!"


if __name__ == "__main__":
    app.run(debug=True)
