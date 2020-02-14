from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return '''<html><head><title>Hello!</title></head><body><h1>Hello!</h1></body></html>'''

if __name__ == "__main__":
    app.run(debug=True)