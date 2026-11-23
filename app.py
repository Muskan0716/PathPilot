
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user
)
from werkzeug.security import generate_password_hash, check_password_hash

from database import db, User, Progress
from career_engine import CAREERS, recommend_careers
from roadmap_generator import generate_roadmap


app = Flask(__name__)

app.config["SECRET_KEY"] = "pathpilot-development-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pathpilot.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# CHECK STUDENT PROFILE
def profile_is_complete(user):
    return bool(
        user.education
        and user.courses
        and user.skills
        and user.career_interests
    )


# STUDENT REDIRECTION
def student_destination():

    if not profile_is_complete(current_user):
        return redirect(url_for("profile"))

    return redirect(url_for("dashboard"))


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# USER REGISTRATION
@app.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return student_destination()

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not name or not email or not password:
            flash("Please fill in all fields.")
            return redirect(url_for("register"))

        if len(password) < 6:
            flash("Password must contain at least 6 characters.")
            return redirect(url_for("register"))

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered. Please login.")
            return redirect(url_for("login"))

        new_user = User(
            name=name,
            email=email,
            password_hash=generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        flash("Registration successful! Complete your profile.")

        return redirect(url_for("profile"))

    return render_template("register.html")


# USER LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return student_destination()

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):

            login_user(user)

            flash("Login successful!")

            return student_destination()

        flash("Invalid email or password.")

    return render_template("login.html")


# USER LOGOUT
@app.route("/logout")
@login_required
def logout():

    logout_user()

    flash("You have logged out.")

    return redirect(url_for("home"))


# STUDENT PROFILE
@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():

    if request.method == "POST":

        education = request.form.get(
            "education", ""
        ).strip()

        courses = request.form.getlist("courses")
        skills = request.form.getlist("skills")
        career_interests = request.form.getlist("career_interests")

        if not education:
            flash("Please select your education.")
            return redirect(url_for("profile"))

        if not courses:
            flash("Please select at least one course.")
            return redirect(url_for("profile"))

        if not skills:
            flash("Please select at least one technical skill.")
            return redirect(url_for("profile"))

        if not career_interests:
            flash("Please select at least one career interest.")
            return redirect(url_for("profile"))

        current_user.education = education
        current_user.courses = ", ".join(courses)
        current_user.interests = ", ".join(courses)
        current_user.skills = ", ".join(skills)
        current_user.career_interests = ", ".join(career_interests)

        db.session.commit()

        flash("Your career profile has been saved!")

        return redirect(url_for("careers"))

    skills_list = [
        "Python", "Java", "C++", "SQL",
        "Machine Learning", "Deep Learning",
        "Data Analysis", "Data Science",
        "HTML", "CSS", "JavaScript", "React",
        "Git", "GitHub", "Excel", "Power BI",
        "Tableau", "TensorFlow", "PyTorch",
        "Flask", "Django", "OOP",
        "Problem Solving", "Data Structures",
        "Algorithms", "Cloud Computing",
        "AWS", "Azure", "MongoDB",
        "MySQL", "PostgreSQL", "REST API",
        "Bootstrap"
    ]

    selected = [
        skill.strip().lower()
        for skill in (current_user.skills or "").split(",")
        if skill.strip()
    ]

    return render_template(
        "profile.html",
        skills_list=skills_list,
        selected=selected
    )


# CAREER RECOMMENDATIONS
@app.route("/careers")
@login_required
def careers():

    if not profile_is_complete(current_user):
        flash("Please complete your profile first.")
        return redirect(url_for("profile"))

    careers_list = recommend_careers(
        current_user.skills or "",
        current_user.career_interests or "",
        current_user.courses or ""
    )

    return render_template(
        "careers.html",
        careers=careers_list
    )


# CAREER ROADMAP
@app.route("/roadmap/<career>")
@login_required
def roadmap(career):

    if not profile_is_complete(current_user):
        flash("Please complete your profile first.")
        return redirect(url_for("profile"))

    selected_career = next(
        (item for item in CAREERS if item["slug"] == career),
        None
    )

    if selected_career is None:
        flash("Career not found.")
        return redirect(url_for("careers"))

    items = generate_roadmap(career)

    existing_tasks = {
        item.task
        for item in Progress.query.filter_by(
            user_id=current_user.id
        ).all()
    }

    for task in items:

        if task not in existing_tasks:

            db.session.add(
                Progress(
                    user_id=current_user.id,
                    task=task,
                    completed=False
                )
            )

            existing_tasks.add(task)

    db.session.commit()

    return render_template(
        "roadmap.html",
        career=selected_career["name"],
        items=items
    )


# STUDENT DASHBOARD / PROGRESS TRACKER
@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():

    if not profile_is_complete(current_user):
        flash("Please complete your profile first.")
        return redirect(url_for("profile"))

    if request.method == "POST":

        task = request.form.get("task", "").strip()

        if task:

            db.session.add(
                Progress(
                    user_id=current_user.id,
                    task=task,
                    completed=False
                )
            )

            db.session.commit()

            flash("Task added successfully!")

        return redirect(url_for("dashboard"))

    progress_items = Progress.query.filter_by(
        user_id=current_user.id
    ).order_by(Progress.id.asc()).all()

    completed = sum(
        1 for item in progress_items if item.completed
    )

    total = len(progress_items)

    percentage = round(
        (completed / total) * 100
    ) if total else 0

    return render_template(
        "dashboard.html",
        progress_items=progress_items,
        completed=completed,
        total=total,
        percentage=percentage
    )


# UPDATE TASK STATUS
@app.route("/progress/<int:item_id>/toggle", methods=["POST"])
@login_required
def toggle_progress(item_id):

    item = Progress.query.filter_by(
        id=item_id,
        user_id=current_user.id
    ).first_or_404()

    item.completed = not item.completed

    db.session.commit()

    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)
