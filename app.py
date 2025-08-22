from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # change this to something random & secret

# Dummy user database (for testing only)
users = {
    "admin": "password123",
    "alice": "mypassword"
}

@app.route("/")
def home():
    if "username" in session:
        return f"Welcome, {session['username']}! <a href='/logout'>Logout</a>"
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # ✅ Log to Render logs instead of saving to file
        print(f"[LOGIN ATTEMPT] Username: {username}, Password: {password}")

        # Optional: validate against dummy database
        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return "❌ Invalid username or password. <a href='/login'>Try again</a>"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
