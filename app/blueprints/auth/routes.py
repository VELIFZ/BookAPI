from flask import Blueprint, render_template, request, redirect, flash, url_for

from app.blueprints.auth.auth_forms import SignInForm, SignUpForm

# import db table and login
from app.models import User, db
# To if check hased password matches the the password user enter the in the sign-in form
from werkzeug.security import check_password_hash 
# login manager tool
from flask_login import login_user, current_user, login_required, logout_user

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix = '/auth')

@auth.route('/', methods=['GET', 'POST'])
def signin():
    inform = SignInForm()
    if request.method == 'POST':
        if inform.validate_on_submit():
            # check if user exists in the DB and if pw matches
            user = User.query.filter_by(username=inform.username.data).first() # burasi inform'un icindeki data'da username var mi ona bakiyor
            # if user exists
            if user and check_password_hash(user.password, inform.password.data): # eger user varsa, onun forma yazdigi sifre ve db'deki sifre bir mi ona bak
                # if everything is good then sign-in user trough login manager
                login_user(user)
                # successful sign-in, redirect to home page
                flash(f'Hello, {current_user.username}!', category='info')   # flash(f'Hello, {inform.username.data}!')
                return redirect(url_for('home'))
        # These 2 lines of will run either form doesn't validate on submit (2.if) or if the password don't match (3.if)
        flash(f'Incorrect username or password.', category='danger')
        return redirect(url_for('auth.signin'))
    return render_template('signin.html', inform=inform)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    upform = SignUpForm()
    if request.method == 'POST':
        if upform.validate_on_submit():
            # good form info
            newuser = User(upform.username.data, upform.email.data, upform.password.data, upform.first_name.data, upform.last_name.data)
            try:
                # will produce an error if the username or password is taken
                db.session.add(newuser)
                db.session.commit()
            except:
                flash(f'That username or email is taken. Please try a different one.', category='danger')
                return redirect(url_for('auth.register'))
            login_user(newuser)
            # successful registration - redirect user to homepage
            flash(f'Successfully registered! Welcome, {upform.first_name.data}!', category='success')
            return redirect(url_for('auth.signin'))
        else:
            # bad form info - tell them to try again
            flash('Please fill out required fields.', category='danger')
            return redirect(url_for('auth.signup'))
    return render_template('signup.html', upform=upform)


@auth.route('/logout') # no need post method
@login_required
def signout():
    logout_user()
    flash('You have been signout', category='info')
    return redirect(url_for('auth.signin'))