from flask import Flask, render_template, request, redirect, session
from models import db, User, Student, Client
from datetime import datetime

app = Flask(__name__)

app.secret_key = "secret123"


# =========================
# DATABASE CONNECTION
# =========================

app.config["SQLALCHEMY_DATABASE_URI"] = \
"mysql+pymysql://root:@localhost/snapwork_db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# ROLE SELECTION PAGE
# =========================

@app.route("/signup")
def signup_page():
    return render_template("signup.html")


# =========================
# STUDENT SIGNUP
# =========================

@app.route("/signup/student", methods=["GET", "POST"])
def student_signup():

    if request.method == "POST":

        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        college = request.form.get("college")
        skill = request.form.get("skill")
        country = request.form.get("country")

        # create user
        user = User(
            email=email,
            password=password,
            role="student",
            created_at=datetime.now()
        )

        db.session.add(user)
        db.session.commit()

        # create student
        student = Student(
            user_id=user.id,
            first_name=first_name,
            last_name=last_name,
            college=college,
            skill=skill,
            country=country
        )

        db.session.add(student)
        db.session.commit()

        return redirect("/login")

    return render_template("studentsignup.html")


# =========================
# CLIENT SIGNUP
# =========================

@app.route("/signup/client", methods=["GET", "POST"])
def client_signup():

    if request.method == "POST":

        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        country = request.form.get("country")

        # create user
        user = User(
            email=email,
            password=password,
            role="client",
            created_at=datetime.now()
        )

        db.session.add(user)
        db.session.commit()

        # create client
        client = Client(
            user_id=user.id,
            first_name=first_name,
            last_name=last_name,
            country=country
        )

        db.session.add(client)
        db.session.commit()

        return redirect("/login")

    return render_template("clientsignup.html")


# =========================
# LOGIN
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        if user:

            session["user_id"] = user.id
            session["role"] = user.role

            if user.role == "client":
                return redirect("/client/dashboard")

            elif user.role == "student":
                return redirect("/student/dashboard")

        else:
            return "Invalid email or password"

    return render_template("login.html")


# =========================
# STUDENT DASHBOARD
# =========================

@app.route("/student/dashboard")
def student_dashboard():

    if session.get("role") != "student":
        return redirect("/login")

    return "Student Dashboard"


# =========================
# CLIENT DASHBOARD
# =========================

@app.route("/client/dashboard")
def client_dashboard():

    if session.get("role") != "client":
        return redirect("/login")

    return "Client Dashboard"


# =========================

if __name__ == "__main__":
    app.run(debug=True)