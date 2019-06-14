from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, I'm Slot API"

if __name__ == "__main__":
    app.run()
