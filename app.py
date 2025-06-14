from flask import Flask, render_template, request
from qrng import generate_quantum_bit

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bit = None
    if request.method == "POST":
        bit = generate_quantum_bit()
    return render_template("index.html", bit=bit)

if __name__ == "__main__":
    app.run(debug=True)
