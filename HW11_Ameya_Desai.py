from prettytable import PrettyTable
from collections import defaultdict


def file_reading_gen(path, fields, sep=',', header=False):
    """checks if the func generates the tuple"""
    try:
        fp = open(path, "r", encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Cant open '{path}' for reading")
    else:
        with fp:
            for offset, line in enumerate(fp, 1):
                current = line.rstrip('\n').split(sep)
                if len(current) != fields:
                    raise ValueError(f"'{path} lines: (n): read {len(current)} fields but expected {fields}")
                elif offset == 1 and header:
                    continue
                else:
                    yield tuple(current)


class Repository:
    """Repository class, container"""

    def __init__(self, path1, path2, path3, path4):
        self.path_majors = path1
        self.path_students = path2
        self.path_grades = path3
        self.path_instructors = path4

        self.required = defaultdict(list)
        self.elective = defaultdict(list)
        self.majors__summery_dict = defaultdict(list)

        self.student_name = defaultdict(str)
        self.student_dept = defaultdict(str)
        self.completed_courses = defaultdict(list)
        self.student_name_dept_courses = defaultdict(list)
        self.remaining_required = defaultdict(list)
        self.remaining_elective = defaultdict(list)
        self.student_summery_dict = defaultdict(list)

        self.course_instructorCWID = defaultdict(str)
        self.course_studentCount = defaultdict(int)
        self.instructor_summery_dict = defaultdict(list)


        self.Major()
        self.Student()
        self.Instructor()


    def Major(self):
        """ Major function. Operetions for creating major summery table are performed here"""
        try:
            for dept, req_elective, course in file_reading_gen(self.path_majors, 3, sep="\t", header=True):
                if req_elective != "R" and req_elective != "E":
                    print("invalid input for required/elective")
                    exit()

                elif req_elective == "R":
                    self.required[dept].append(course)

                elif req_elective == "E":
                    self.elective[dept].append(course)

            self.majors_summery_dict = {k: [self.required[k], self.elective[k]] for k in self.required}  #merging two dictionaries


        except ValueError as ve:
            print(ve)
            exit()
        except FileNotFoundError as fnfe:
            print(fnfe)
            exit()




    def Student(self):
        try:
            """ Student function. Operetions for creating student summery table are performed here"""
            for CWID, name, major in file_reading_gen(self.path_students, 3, sep="\t", header=True):
                self.student_name[CWID] = name
                self.student_dept[CWID] = major


            for student_CWID, course, grade, instructor_cwid in file_reading_gen(self.path_grades, 4, sep="\t", header=True):
                if grade != "F":
                    self.completed_courses[student_CWID].append(course)

            self.student_name_dept_courses = {k: [self.student_name[k], self.student_dept[k], self.completed_courses[k]] for k in self.student_name}


            for k, v in self.majors_summery_dict.items():
                for key, val in self.student_name_dept_courses.items():
                    if k == val[1]:
                        a = [i for i in v[0] if i not in val[2]]
                        for i in a:
                            self.remaining_required[key].append(i)


            for k, v in self.majors_summery_dict.items():
                for key, val in self.student_name_dept_courses.items():
                    if k == val[1]:
                        a = [i for i in v[1] if i not in val[2]]
                        if len(a) == len(v[1]):
                            for i in v[1]:
                                self.remaining_elective[key].append(i)
                        else:
                            self.remaining_elective[key].append(None)


            self.student_summery_dict = {k: [self.student_name[k], self.student_dept[k], self.completed_courses[k], self.remaining_required[k], self.remaining_elective[k]] for k in self.student_name}


        except ValueError as ve:
            print(ve)
            exit()
        except FileNotFoundError as fnfe:
            print(fnfe)
            exit()




    def Instructor(self):
        """ Major function. Operetions for creating Instructor summery table are performed here"""
        try:
            for studentCWID, course, grade, instructorCWID in file_reading_gen(self.path_grades, 4, sep="\t", header=True):
                self.course_instructorCWID[(course,instructorCWID)] = instructorCWID
                self.course_studentCount[(course,instructorCWID)] += + 1

            self.instructor_summery_dict = {k: [self.course_instructorCWID[k], self.course_studentCount[k]] for k in self.course_instructorCWID} # merging two dictionaries


            for CWID, instructor, dept in file_reading_gen(self.path_instructors, 3, sep="\t", header=True):
                 for k, v in self.instructor_summery_dict.items():
                     if v[0] == CWID:
                         self.instructor_summery_dict[k].append(instructor)
                         self.instructor_summery_dict[k].append(dept)

        except ValueError as ve:
             print(ve)
             exit()
        except FileNotFoundError as fnfe:
             print(fnfe)
             exit()




    def pretty_print(self):
        """ prints prettytable """

        """Prints majors summery table"""
        pt = PrettyTable(field_names=['Dept', 'Required', 'Electives'])
        for key, val in self.majors_summery_dict.items():
            pt.add_row([key, sorted(val[0]), sorted(val[1])])
        print(pt)

        """Prints students summery table"""
        pt = PrettyTable(field_names=['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining required',
                                      'Remaining Electives'])
        for key, val in self.student_summery_dict.items():
            pt.add_row([key, val[0], val[1], sorted(val[2]), sorted(val[3]), sorted(val[4])])
        print(pt)

        """Prints Instructor summery table"""
        pt = PrettyTable(field_names=['Cwid', 'Name', 'Dept', 'Course', 'Students'])
        for key, val in self.instructor_summery_dict.items():
            pt.add_row([val[0], val[2], val[3], key[0], val[1]])
        print(pt)


def main():
    Repository('D:/majors_11.txt', 'D:/students_11.txt', 'D:/grades_11.txt', 'D:/instructors_11.txt').pretty_print()