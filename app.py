from flask import Flask, render_template, request

app = Flask(__name__)

coeffs = {
    "FR": 3,
    "MATHS": 5,
    "PC": 4,
    "SVT": 2,
    "ESP/ALL": 1,
    "ANG": 3,
    "HG": 2,
    "MUS": 1,
    "EPS": 1,
    "COND": 1
}

@app.route("/", methods=["GET", "POST"])
def index():
    moyenne = None

    if request.method == "POST":
        notes = {}
        for mat in coeffs:
            notes[mat] = float(request.form.get(mat, 0))

        somme = sum(notes[m] * coeffs[m] for m in coeffs)
        moyenne = somme / 23

    return render_template("index.html", coeffs=coeffs, moyenne=moyenne)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    