# ------------------------------------------------------------------
# pyinstaller -F --add-data "templates;templates" --add-data "static;static" main.py
# ------------------------------------------------------------------

import os
import sys
from flask import Flask, render_template, request, jsonify
from flaskwebgui import FlaskUI

from classes.checkin_procs import validateCheckin
from sqlite.sqlite_students import GetSqliteStudents

base_dir = '.'
if hasattr(sys, '_MEIPASS'):
    base_dir = os.path.join(sys._MEIPASS)

app = Flask(__name__, static_folder=os.path.join(base_dir, 'static'), template_folder=os.path.join(base_dir, 'templates'))

@app.route('/')
def index():
    checkinMessage = {
        "imageSrc" : "static/images/misc_images/RSM_Logo1.jpg",
        "message"  : "Waiting ...",
        "responseClass" : "fw-bold border-bottom error"}
    return render_template('index.html', checkinMessage=checkinMessage)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/checkin', methods=['POST'])
def checkin():
    if request.method == 'POST':
        data = request.form.to_dict()
        #print("Received data:", data)
        return jsonify(validateCheckin(request.form.to_dict()))

@app.route('/students')
def students():
    db_path = os.path.join(os.getenv('APPDATA'), 'Attendance', 'AttendanceV2.db')
    student_records = GetSqliteStudents(db_path)
    return render_template('students.html', data=student_records)

# Run the application
if __name__ == '__main__':
    #ui = FlaskUI(app=app, width=1200, height=900, fullscreen=False, server='flask')
    #ui.run()
    app.run(debug=False)