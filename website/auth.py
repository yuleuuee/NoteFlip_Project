from flask import Blueprint,request,flash , redirect ,url_for
from flask import render_template
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash #just to secure the password
from . import db
from flask_login import login_user,login_required,logout_user,current_user
from flask import session

import bcrypt

auth = Blueprint('auth',__name__)

#******************************************************************** LOG_IN ***********************************************************#

#they are our roots : which are like different webapages
@auth.route('/login', methods =['GET','POST']) # this means we can accetp the get and post request
def login(): 
    # email = request.form.get('email')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

         # If login is successful, set a session variable indicating the user is logged in
        session['logged_in'] = True

        #checking if the email is there in database, before logining in :
        user = User.query.filter_by(email= email).first()
        if user:
            if len(password) == 0:
                flash('Must Enter Password!!!', category='error')
                return render_template("login.html",user = current_user,returned_email = email)
            else:
                # if check_password_hash(user.password, password): #verifies if the plaintext password matches the stored hashed password.
                #     flash('Successfully logged in!',category='success')
                #     #will remember usnless the server get restarted
                #     login_user(user,remember=True) # remembers the logedIN user until user dont clear the browsing histry or seession
                #     return redirect(url_for('views.content'))
                # else:
                #     flash('Incorrect Password, try again!!',category='error')
                #     return render_template("login.html",user = current_user,returned_email = email)

                #checking  salts from both ways 
                if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                    flash('Successfully logged in!', category='success')
                    # Remember the logged-in user until the session is cleared
                    login_user(user, remember=True)
                    return redirect(url_for('views.content'))
                else:
                    flash('Incorrect Password, try again!!', category='error')
                    return render_template("login.html", user=current_user, returned_email=email)
        else:
            if len(email) == 0:
                flash('Must Enter Email !!',category='error')
            elif "@" not in email:
                flash("Email must contain '@' ",category='error')
            elif not (("." in email) and (email.count(".") > 0)): # verifies if there's at least one dot (".") in the email
                flash("Invalid email format", category='error')
            else:
                flash('Email does not exists!!',category='error')
                #not wrting the rendering page will render the current page after error message

    return render_template("login.html",user = current_user)


#******************************************************************** LOG_OUT ***********************************************************#

@auth.route('/logout')
@login_required # this make sure that we must login ,before logging out (we can't log out if we aren't even login)
def logout():

    session.clear()
    logout_user()
    flash('Successfully Logged out',category='success')
    return redirect(url_for('auth.login'))

       


#******************************************************************** SIGN_UP ***********************************************************#
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #checking if the email already exists before Signing Up :

        user = User.query.filter_by(email= email).first() # give the user data ,(which shows there is a user with the same email you entered while signing in )

        if user: # that means if there's a user having the email you are entering then
            flash('Email already Exists',category='error')
        elif len(email)==0:
            flash("Must Enter Email",category='error')
        elif "@" not in email:
            flash("Email must contain @ ",category='error')
        elif not (("." in email) and (email.count(".") > 0)): # verifies if there's at least one dot (".") in the email
            flash("Invalid email format", category='error')
        elif len(email) < 4:
            flash("Email must be greater than 3 characters!!",category='error')
        elif len(first_name) < 3:
            flash("First Name must be greater than 3 characters!!",category='error')
        elif first_name.isdigit():
            flash("First Name can't just be numbers!!",category='error')
        elif len(password1)>12:
             flash("Password must be less than 12 characters!!",category='error')
        elif password1 != password2:
            flash("Password dosen't match!!",category='error')
        elif len(password1) < 4:
            flash("Password must be at least 4 characters!!",category='error')
        else:
            new_user = User(email=email,first_name = first_name,password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt()))
            # new_user = User(email=email,first_name = first_name,password = generate_password_hash(password1)) # sha256 : is just a hashing algorithm
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user,remember=True) # used to log in a user after they have successfully provided their credentials
            flash("Account Created Succesfully!",category='success')
            return redirect(url_for('views.content')) # where to redirect after successful signin

    return render_template("signup.html",user = current_user) # this is true


# WAYS FOR PASSWORD VALLIDATION

# if len(password) < 8:
#         flash("Password must be at least 8 characters long", category='error')
#     elif not any(char.isupper() for char in password):
#         flash("Password must contain at least one uppercase letter", category='error')
#     elif not any(char.islower() for char in password):
#         flash("Password must contain at least one lowercase letter", category='error')
#     elif not any(char.isdigit() for char in password):
#         flash("Password must contain at least one digit", category='error')
#     elif not any(not char.isalnum() for char in password):
#         flash("Password must contain at least one special character", category='error')

#********************************************************************  ***********************************************************#
