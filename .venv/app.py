from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "drink more coffee right now"

app.run(host="0.0.0.0", port=5000)


