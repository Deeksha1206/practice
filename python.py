from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask Backend!"

if __age__ == "__main__":
    app.run(debug=True)
