from flask import Flask

app = Flask(__name__)
app.config['TESTING'] = True 

@app.route("/")
def hello_world():
    return "<p>Hello, !</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Change host to 0.0.0.0
