from flask import Flask, render_template, request, redirect # pyright: ignore[reportMissingImports]
import sqlite3

app = Flask(__name__)

# DATABASE CONNECTION
def get_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# HOME PAGE
@app.route("/")
def home():
    return render_template("pg1.html")


# LOGIN PAGE
@app.route("/login")
def login():
    return render_template("login.html")


# SIGNUP
@app.route("/signup", methods=["POST"])
def signup():

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    conn = get_connection()

    conn.execute(
        "INSERT INTO users (name,email,password) VALUES (?,?,?)",
        (name,email,password)
    )

    conn.commit()
    conn.close()

    return redirect("/")


# LOGIN CHECK
@app.route("/login_user", methods=["POST"])
def login_user():

    email = request.form["email"]
    password = request.form["password"]

    conn = get_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email,password)
    ).fetchone()

    conn.close()

    if user:
        return redirect("/submit")
    else:
        return "Invalid Login"


# SUBMIT PAGE
@app.route("/submit")
def submit():
    return render_template("submit.html")

# SAVE OCEAN DATA
@app.route("/submit_data", methods=["POST"])
def submit_data():

    location = request.form["location"]
    temperature = float(request.form["temperature"])
    species = request.form["species"]

    print(location, temperature, species)

    conn = get_connection()

    conn.execute(
        "INSERT INTO ocean_data (location, temperature, species) VALUES (?, ?, ?)",
        (location, temperature, species)
    )

    conn.commit()
    conn.close()

    return redirect("/dashboard")

#Dashboard
@app.route("/dashboard")
def dashboard():

    conn = get_connection()

    data = conn.execute(
        "SELECT * FROM ocean_data"
    ).fetchall()

    conn.close()

    return render_template("dashboard.html", data=data)

#Delete a specific record
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    conn = get_connection()

    conn.execute("DELETE FROM ocean_data WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect("/dashboard")


#About
@app.route("/about")
def about():
    return render_template("about.html")
#Logout
@app.route("/logout")
def logout():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)