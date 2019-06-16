from flask import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, I'm Dice API"

if __name__ == "__main__":
    app.run()
