from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")   # Flask looks in templates/index.html

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Save credentials to logins.txt
        with open("logins.txt", "a") as f:
            f.write(f"Username: {username}, Password: {password}\n")

        return "✅ Login successful (credentials saved)!"

    # If user visits /login directly with GET
    return "📌 Please use the form on the homepage to log in."

if __name__ == "__main__":
    app.run(debug=True)
