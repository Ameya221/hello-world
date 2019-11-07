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


class Student:
    """ Student class"""

    def __init__(self, path):
        """ self function"""
        self.path1 = path
        self.d1 = defaultdict(list)
        self.d2 = defaultdict(list)
        self.dfinal = defaultdict(list)
        self.analyze_files()



    def analyze_files(self):
        """ File analyze function. amost of the operetions are performed here"""
        for line in file_reading_gen(self.path1, 3, sep="\t", header=True):

            if line[0] == "SFEN" and line[1] == "R":
                self.d1[line[0]].append(line[2])               # adds required courses of  SFEN branch

            elif line[0] == "SYEN" and line[1] == "R":
                self.d1[line[0]].append(line[2])               # adds required courses of  SYEN branch

            elif line[0] == "SFEN" and line[1] == "E":
                self.d2[line[0]].append(line[2])               # adds elective courses of  SFEN branch

            elif line[0] == "SYEN" and line[1] == "E":
                self.d2[line[0]].append(line[2])               # adds elective courses of  SYEN branch

        self.dfinal = {k: [self.d1[k], self.d2[k]] for k in self.d1}  # merges d1 and d2


    def pretty_print(self):
        """ prints prettytable """
        pt = PrettyTable(field_names=['Dept', 'Required', 'Electives'])
        for key, val in self.dfinal.items():
            pt.add_row([key, sorted(val[0]), sorted(val[1])])
        print(pt)




class Summery:

    def __init__(self, path1, path2, path3):

        self.path1 = path1
        self.path2 = path2
        self.path3 = path3

        self.d1 = defaultdict(str)
        self.d2 = defaultdict(str)
        self.d3 = defaultdict(list)
        self.d123 = defaultdict(list)
        self.d4 = defaultdict(list)
        self.d5 = defaultdict(list)
        self.dfinal = defaultdict(list)

        self.dn1 = defaultdict(list)
        self.dn2 = defaultdict(list)
        self.dnf = defaultdict(list)
        self.analyze_files()

    def analyze_files(self):
        """ File analyze function. amost of the operetions are performed here"""
        for line in file_reading_gen(self.path1, 3, sep=";", header=True):

            self.d1[line[0]] = line[1]
            self.d2[line[0]] = line[2]



        for line in file_reading_gen(self.path2, 4, sep="|", header=True):

            if line[2] != "F":
                self.d3[line[0]].append(line[1])


        self.d123 = {k: [self.d1[k], self.d2[k], self.d3[k]] for k in self.d1}




        for line in file_reading_gen(self.path3, 3, sep="\t", header=True):

            if line[0] == "SFEN" and line[1] == "R":
                self.dn1[line[0]].append(line[2])

            elif line[0] == "SYEN" and line[1] == "R":
                self.dn1[line[0]].append(line[2])

            elif line[0] == "SFEN" and line[1] == "E":
                self.dn2[line[0]].append(line[2])

            elif line[0] == "SYEN" and line[1] == "E":
                self.dn2[line[0]].append(line[2])


        self.dnf = {k: [self.dn1[k], self.dn2[k]] for k in self.dn1}


        for k, v in self.dnf.items():
            for key, val in self.d123.items():
                if k == val[1]:
                    a = [i for i in v[0] if i not in val[2]]
                    for i in a:
                        self.d4[key].append(i)


        for k, v in self.dnf.items():
            for key, val in self.d123.items():
                if k == val[1]:
                    a = [i for i in v[1] if i not in val[2]]
                    if len(a) == 3:
                        for i in v[1]:
                            self.d5[key].append(i)
                    else:
                        self.d5[key].append(None)


        self.dfinal = {k: [self.d1[k], self.d2[k], self.d3[k], self.d4[k], self.d5[k]] for k in self.d1}


    def pretty_print(self):
        """ prints prettytable """
        pt = PrettyTable(field_names=['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining required', 'Remaining Electives'])
        for key, val in self.dfinal.items():
            pt.add_row([key, val[0], val[1], sorted(val[2]), sorted(val[3]), sorted(val[4])])
        print(pt)



class Instructor:
    def __init__(self, path, path2):
        """ self function"""
        self.path1 = path
        self.path2 = path2
        self.d1 = defaultdict(str)
        self.d2 = defaultdict(int)
        self.dfinal = defaultdict(list)
        self.analyze_files()



    def analyze_files(self):
        """ File analyze function. amost of the operetions are performed here"""
        for line in file_reading_gen(self.path1, 4, sep="|", header=True):
            self.d1[line[1]] = line[3]
            self.d2[line[1]] += + 1

        self.dfinal = {k: [self.d1[k], self.d2[k]] for k in self.d1}


        for line in file_reading_gen(self.path2, 3, sep="|", header=True):
            for  k, v in self.dfinal.items():
                if v[0] == line[0]:
                    self.dfinal[k].append(line[1])
                    self.dfinal[k].append(line[2])



    def pretty_print(self):
        """ prints prettytable """
        pt = PrettyTable(field_names=['Cwid', 'Name', 'Dept', 'Course', 'Students'])
        for key, val in self.dfinal.items():
            pt.add_row([val[0], val[2], val[3], key, val[1]])
        print(pt)

def main():
    Student('D:/majors.txt').pretty_print()
    Summery('D:/student.txt','D:/course.txt','D:/majors.txt').pretty_print()
    Instructor( 'D:/course.txt', 'D:/instructor.txt').pretty_print()