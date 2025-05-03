from flask import Flask, render_template, request
import os

app = Flask(__name__)

def slow_text(text, delay=0.1):
    # This function can be used for visual effects if needed later
    return ''.join(char for char in text)

@app.route("/", methods=["GET", "POST"])
def birthday():
    if request.method == "POST":
        name = request.form["name"]
        return render_template("surprise.html", name=name)
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)