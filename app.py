import random
from flask import *

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html", title="Dice API");

@app.route("/roll", methods=['GET', 'POST'])
def roll():
    if request.method == 'GET': 
        faces = request.args.get('faces')
        cnt = request.args.get('cnt')
        times = request.args.get('times')

    elif request.method == 'POST': 
        faces = request.json['faces']
        cnt = request.json['cnt']
        times = request.json['times']

    faces = int(faces)
    cnt = int(cnt)
    times = int(times)
    
    result = []
    for t in range(times):

        r = []
        for c in range(cnt):
            top = random.randint(1, faces)
            r.append(top)

        result.append(r)

    data = [
        {"faces": faces},
        {"cnt": cnt},
        {"times": times},
        {"result": result}
    ]
            
    return jsonify({
        "status": "OK",
        "data": data
        })

if __name__ == "__main__":
    app.run()
