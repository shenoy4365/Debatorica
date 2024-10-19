# from flask import Blueprint, render_template, request, flash, jsonify
# from flask_login import login_required, current_user
# from .models import Note
# from . import db
# import json

# views = Blueprint('views', __name__)


# @views.route('/', methods=['GET', 'POST'])
# @login_required
# def home():
#     if request.method == 'POST': 
#         note = request.form.get('note')#Gets the note from the HTML 

#         if len(note) < 1:
#             flash('Note is too short!', category='error') 
#         else:
#             new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
#             db.session.add(new_note) #adding the note to the database 
#             db.session.commit()
#             flash('Note added!', category='success')

#     return render_template("home.html", user=current_user)

# @views.route('/landingpage')
# def landingpage():
#     return render_template('landingpage.html', user=current_user)

# @views.route('/sign-up')
# def sign_up():
#     return render_template('sign_up.html', user=current_user)

# @views.route('/login')
# def login():
#     return render_template('login.html', user=current_user)

# @views.route('/delete-note', methods=['POST'])
# def delete_note():  
#     note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()

#     return jsonify({})

# import os
# from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
# from flask_login import login_required, current_user
# from werkzeug.utils import secure_filename
# from .models import Note
# from . import db
# import json
# from website.analysis.pdf_text_extraction import extract_text_from_pdf  # Importing the text extraction function

# views = Blueprint('views', __name__)

# # Allowed file extensions for upload
# ALLOWED_EXTENSIONS = {'pdf'}

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @views.route('/', methods=['GET', 'POST'])
# @login_required
# def home():
#     if request.method == 'POST' and 'note' in request.form:
#         note = request.form.get('note')

#         if len(note) < 1:
#             flash('Note is too short!', category='error') 
#         else:
#             new_note = Note(data=note, user_id=current_user.id)
#             db.session.add(new_note)
#             db.session.commit()
#             flash('Note added!', category='success')

#     return render_template("home.html", user=current_user)

# @views.route('/upload-pdf', methods=['POST'])
# @login_required
# def upload_pdf():
#     if 'pdf_file' not in request.files:
#         flash('No file part', category='error')
#         return redirect(request.url)

#     file = request.files['pdf_file']

#     if file.filename == '':
#         flash('No selected file', category='error')
#         return redirect(request.url)

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         filepath = os.path.join('uploads', filename)
#         file.save(filepath)

#         # Extract text from the uploaded PDF
#         extracted_text = extract_text_from_pdf(filepath)

#         # Add extracted text as a new note
#         new_note = Note(data=extracted_text, user_id=current_user.id)
#         db.session.add(new_note)
#         db.session.commit()

#         flash('PDF uploaded and text extracted successfully!', category='success')
#         return redirect(url_for('views.home'))
#     else:
#         flash('Invalid file type. Only PDFs are allowed.', category='error')
#         return redirect(request.url)

# @views.route('/landingpage')
# def landingpage():
#     return render_template('landingpage.html', user=current_user)

# @views.route('/sign-up')
# def sign_up():
#     return render_template('sign_up.html', user=current_user)

# @views.route('/log-in')
# def login():
#     return render_template('login.html', user=current_user)

# @views.route('/delete-note', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data)
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()

#     return jsonify({})

import os
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from io import BytesIO
from .models import Note
from . import db
import json
from website.analysis.pdf_text_extraction import extract_text_from_pdf  # Importing the text extraction function

views = Blueprint('views', __name__)

# Allowed file extensions for upload
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST' and 'note' in request.form:
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/upload-pdf', methods=['POST'])
@login_required
def upload_pdf():
    if 'pdf_file' not in request.files:
        flash('No file part', category='error')
        return redirect(request.url)

    file = request.files['pdf_file']

    if file.filename == '':
        flash('No selected file', category='error')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Process the file in memory using a BytesIO object
        file_bytes = BytesIO(file.read())  # Read the file data into memory

        # Extract text from the uploaded PDF (using the in-memory file)
        extracted_text = extract_text_from_pdf(file_bytes)

        # Add extracted text as a new note
        new_note = Note(data=extracted_text, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()

        flash('PDF uploaded and text extracted successfully!', category='success')
        return redirect(url_for('views.home'))
    else:
        flash('Invalid file type. Only PDFs are allowed.', category='error')
        return redirect(request.url)

@views.route('/landingpage')
def landingpage():
    return render_template('landingpage.html', user=current_user)

@views.route('/sign-up')
def sign_up():
    return render_template('sign_up.html', user=current_user)

@views.route('/log-in')
def login():
    return render_template('login.html', user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

