import os
from flask import Flask, render_template, request
from qrng import generate_quantum_bit  # This should return a string like '01101001'

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bit = None
    bit_counts = None

    if request.method == "POST":
        bit = generate_quantum_bit(8)  # Generate 8 quantum bits as a string

        # Count how many 0s and 1s are in the 8-bit string
        bit_counts = {
            "0": bit.count("0"),
            "1": bit.count("1")
        }

    return render_template("index.html", bit=bit, bit_counts=bit_counts)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default to 10000 for local dev
    app.run(debug=True, host="0.0.0.0", port=port)
