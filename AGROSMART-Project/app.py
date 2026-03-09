from flask import Flask, render_template, request, redirect, flash
from database import get_connection

app = Flask(__name__)
app.secret_key = "super_secret_key"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save_profile", methods=["POST"])
def save_profile():
    try:
        name = request.form.get("name")
        location = request.form.get("location")
        phone = request.form.get("phone")
        farmSize = request.form.get("farmSize")
        soilPh = request.form.get("soilPh")
        soilType = request.form.get("soilType")

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO farmers
            (name, location, phone, farm_size, soil_ph, soil_type)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (name, location, phone, farmSize, soilPh, soilType))

        conn.commit()
        cur.close()
        conn.close()

        flash("Profile Saved Successfully!", "success")
        return redirect("/dashboard")

    except Exception as e:
        print("Error:", e)
        flash("Something went wrong!", "danger")
        return redirect("/")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

@app.route("/crop_advisor")
def crop_advisor():
    return render_template("crop_advisor.html")

@app.route("/irrigation")
def irrigation():
    return render_template("irrigation.html")

@app.route("/yield_calculator")
def yield_calculator():
    return render_template("yield_calculator.html")

@app.route("/ai_diagnosis")
def ai_diagnosis():
    return render_template("ai_diagnosis.html")


if __name__ == "__main__":
    app.run(debug=True)
