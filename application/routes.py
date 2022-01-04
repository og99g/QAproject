from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.helpers import url_for
from application import app, db
from application.model import User, Note
from application.form import TaskForm

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user

routes = Blueprint('views', __name__)

@app.route('/')
def home():
    all_notes = Note.query.all()
    return render_template("home.html", title="Home",all_notes=all_notes)

@app.route('/about')
def about():
    return render_template("about.html", title="about")


@app.route('/create-task', methods=['GET','POST'])
def creat_task():
    form = TaskForm()
    if request.method == "POST":
        new_notes =Note(description=form.description.data)
        db.session.add(new_notes)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("create-task.html", title="create-task", form=form)

    
@app.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", title="Login")

@app.route('/logout')
def logout():
    return render_template("logout.html", title="Logout")

@app.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        
        if len(email) < 4:
            flash ('EMAIL must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash ('first name  must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash ('passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash ('password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('home'))

    return render_template("sign-up.html", user=current_user)