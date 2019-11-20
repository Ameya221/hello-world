import sqlite3
from flask import Flask, render_template

app = Flask(__name__,  template_folder='D:/New folder/templates')

@app.route('/Hello')
def hello():
    return "Hello world, this is flask"


@app.route('/Instructor_table')
def instructors():
    dbpath = 'D:/sqlite-tools-win32-x86-3300100/Ameya.db'

    try:
        db = sqlite3.connect(dbpath)

    except sqlite3.OperationalError:
        return f"Error: Unable t oopen database at {dbpath}"

    else:
        query = """ select InstructorCWID, name, Dept, Course,count(*) as no_of_students  from grades_11 join instructors_11 on grades_11.InstructorCWID = instructors_11.CWID
                    group by InstructorCWID, Course """

        data = [{'CWID': CWID,'Name': Name, 'Dept': Dept, 'Course': Course, 'No_of_students': No_of_students }
                 for CWID, Name, Dept, Course, No_of_students in db.execute(query)]

        db.close()

        return render_template('instructor.html',
                               my_header="My Stevens Repository",
                               my_param="Instructor summery table",
                               instructors = data)

app.run(debug = True)