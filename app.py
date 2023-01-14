from flask import Flask, render_template, request

app = Flask(__name__)

BASE_URL = "127.0.0.1:5000"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get('user')
        password = request.form.get('password')
        if user == "admin" and password == "password":
            return "success"
        else:
            return render_template("login.html")
    return render_template("login.html")

if __name__ == "__main__":
    app.run()