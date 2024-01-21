from flask import Blueprint,redirect ,url_for
from flask import render_template, request,flash
from flask_login import login_required,current_user
from .models import Note,User
from . import db
import json
from flask import session
from datetime import datetime
from werkzeug.security import generate_password_hash


# Blueprint_name
views = Blueprint('views',__name__)

#******************************************************************** HOME_PAGE ***********************************************************#

@views.route('/')
def home():
    # Retrieve the message from the query parameters
    message01 = request.args.get('message')
   
    
    return render_template("home.html",message = message01)

    # return render_template("home.html",message = message01)


#******************************************************************** CONTENT_PAGE ***********************************************************#

@views.route('/content',methods=['GET','POST'])
@login_required # # Ensure the route is protected, accessible only to authenticated users
def content():

    today_date = datetime.now().date()
    

     # <!--{{greeting}} : use this to make a greating to user acc to the current time-->
    current_time = datetime.now().time()
    if current_time.hour < 12:
        greeting = "Good morning"
    elif current_time.hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    # getting note from form and adding to database and then showing redirectiong to "content page"
    # Sort the notes by date in reverse chronological order
    if request.method =='POST':
        note = request.form.get('note')

        if len(note)<1 :
            flash("You can't add a blank note!!",category='error')
        elif all(char.isspace() for char in note):
            flash("Must Enter some text!!",category='error')
        else:
           
            new_note = Note(data=note,user_id = current_user.id)
            # adding the new note to the Note table of the database
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added Succesfully!',category='success')
    
    
    return render_template("content.html",user = current_user, today_date = today_date, greeting = greeting)




#******************************************************************** DELETE_NOTE ***********************************************************#

#  ********************* deleting just using jinga2 *************************
@views.route('/delete_note/<int:note_id>', methods=['GET','POST'])
@login_required # Ensure the route is protected, accessible only to authenticated users
def delete_note(note_id):

    # searching the note from the 'Note' table from the databese by the help of the 'note id' and giving to a variable naming "note_to_delete"
    note_to_delete = Note.query.filter_by(id=note_id, user_id=current_user.id).first()

    # if the the note of that id is founfd then ....delet that note from databese
    if note_to_delete:
        db.session.delete(note_to_delete)
        db.session.commit()
        flash('Note deleted Successfully!', category='success')
    else:
        flash('Note not found !!',category= 'error')

    return redirect(url_for('views.content'))


#******************************************************************** DELETE_ACCOUNT ***********************************************************#

@views.route('/delete_account',methods=['POST']) #to handle the account deletion process
@login_required # Ensure the route is protected, accessible only to authenticated users
def delete_account():
    if request.method == 'POST':
        # Delete user-related data (here : notes)
        Note.query.filter_by(user_id=current_user.id).delete()

        # Delete the user account
        db.session.delete(current_user)
        db.session.commit()

        # Redirect to the homepage or logout the user
    return redirect(url_for('views.home',message="Account Deleted Successfully!"))

    # To handle GET request or other cases
    # We can also render a confirmation page before deletion

#******************************************************************** EDIT_NOTE ***********************************************************#

@views.route('/update/<int:note_id>', methods=['GET', 'POST'])
@login_required # Ensure the route is protected, accessible only to authenticated users
def update_note(note_id):
    
    today_date = datetime.now()
    note_to_update = Note.query.get_or_404(note_id)
    
    if request.method == "POST":

        new_text = request.form['text_for_update']
        
        # note_to_update.data = request.form['text_for_update']
        if new_text == note_to_update.data:
            flash("No changes were made.", category="error")
            return redirect(url_for('views.content'))     
        elif  len(new_text) ==0 :
            flash("Can't add a blank note!!",category='error')
            return redirect(url_for('views.content'))
        elif all(char.isspace() for char in new_text):
            flash("Must Enter some text!!",category='error')
            return redirect(url_for('views.content'))
        else:
            note_to_update.data = new_text
            note_to_update.date = today_date
            db.session.commit()
            flash('Note Updated Successfully !', category='success')
            return redirect(url_for('views.content'))
    else:
        return render_template('update.html',note_to_update=note_to_update,user = current_user,today_date =today_date )

#******************************************************************** forgot_password  ***********************************************************#
    
@views.route('/forgot_password',methods=['GET','POST'])
def forgot_password():

    if request.method =='POST':
        email = request.form.get('forg_email')
        password01 = request.form.get('forg_pass01')
        password02 = request.form.get('forg_pass02')

        user = User.query.filter_by(email= email).first() # getting the user whose email maches
        
        if user:
            if password01 != password02:
                flash("Password dosen't match!!",category='error')
                return redirect(url_for('auth.login'))
            elif len(password01) == 0 or len(password02)==0:
                flash('Must Enter Password!!!', category='error')
                return redirect(url_for('auth.login'))
            else:
                user.password = generate_password_hash(password01)
                db.session.commit()
                flash('Password successfully modified.', category='success')
                return redirect(url_for('auth.login'))
        else:
            if len(email)==0 and len(password01)==0 and len(password02)==0:
                flash('No Inputs were made!', category='error')
                return redirect(url_for('auth.login'))
            elif len(email)==0:
                flash("Must Enter Email!",category='error')
                return redirect(url_for('auth.login'))
            elif ("@" not in email) or (not (("." in email) and (email.count(".") > 0))):
                flash("Invalid email format!",category='error')
                return redirect(url_for('auth.login'))
            else:
                flash('Email does not exists!', category='error')
                return redirect(url_for('auth.login'))

    return redirect(url_for('auth.login'))

#******************************************************************** forgot_password  ***********************************************************#
@views.route('/change_password',methods=['GET','POST'])
def change_password():
    if request.method =='POST':
        email = request.form.get('your_email')
        password01 = request.form.get('new_pass01')
        password02 = request.form.get('new_pass02')

        user = User.query.filter_by(email= email).first() # getting the user whose email maches
        if current_user==user:
            if password01 != password02:
                flash("Password dosen't match!!",category='error')
                return redirect(url_for('views.content'))
            elif len(password01) == 0 or len(password02)==0:
                flash('Must Enter Password!!!', category='error')
                return redirect(url_for('views.content'))
            else:
                user.password = generate_password_hash(password01)
                db.session.commit()
                flash('Password successfully modified.', category='success')
                return redirect(url_for('views.content'))
        else:
            if len(email)==0 and len(password01)==0 and len(password02)==0:
                flash('No Inputs were made!', category='error')
                return redirect(url_for('views.content'))
            elif len(email)==0:
                flash("Must Enter Email!",category='error')
                return redirect(url_for('views.content'))
            elif ("@" not in email) or (not (("." in email) and (email.count(".") > 0))):
                flash("Invalid email format!",category='error')
                return redirect(url_for('views.content'))
            else:
                flash('You must enter email of this account', category='error')
                return redirect(url_for('views.content'))

    return redirect(url_for('views.content'))