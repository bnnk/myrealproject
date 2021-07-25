from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from ..models.user import User
from app.forms import *
from werkzeug.security import generate_password_hash, check_password_hash

blueprint = Blueprint('pages', __name__)


################
#### routes ####
################


@blueprint.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@blueprint.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@blueprint.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        print("Gota")
        if form.validate_on_submit():
            user = User.objects(name= form.name.data).first()
            if user != None:
                if check_password_hash(user.password, form.password.data):
                    login_user(user, remember=form.remember_me.data)
                    flash("Sucessfully logged in", "success")
                    return redirect(url_for(".home"))
                else:
                    flash("Invalid Password", "danger")
                    return render_template('forms/login.html', form=form)
            else:
                flash("Invalid Username", "danger")
                return render_template('forms/login.html', form=form)
    return render_template('forms/login.html', form=form)


@blueprint.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@blueprint.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

@blueprint.route("/logout")
def logout():
    logout_user()
    flash("Logged out successfully!", "success")
    return redirect(url_for(".home"))