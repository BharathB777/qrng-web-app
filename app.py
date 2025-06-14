import os
from flask import Flask, render_template, request
from qrng import generate_quantum_bit

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bit = None
    if request.method == "POST":
        bit = generate_quantum_bit(8)
    return render_template("index.html", bit=bit)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default to 10000 for local dev
    app.run(debug=True, host="0.0.0.0", port=port)
