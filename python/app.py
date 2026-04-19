from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    score = 0

    love = request.form["love"]
    ring = request.form["ring"]

    if love.lower() == "yes":
        score += 1

    if ring.lower() == "yes":
        score += 1

    return render_template("result.html", score=score)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)    