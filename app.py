import os
from flask import Flask, render_template, request
from qrng import generate_quantum_bit

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bit = None
    bit_counts = None
    bit_length = 8  # default value

    if request.method == "POST":
        try:
            bit_length = int(request.form.get("bit_length", 8))
            bit = generate_quantum_bit(bit_length)
            bit_counts = {
                "0": bit.count("0"),
                "1": bit.count("1")
            }
        except Exception as e:
            bit = f"Error: {str(e)}"

    return render_template("index.html", bit=bit, bit_counts=bit_counts, bit_length=bit_length)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=True, host="0.0.0.0", port=port)
