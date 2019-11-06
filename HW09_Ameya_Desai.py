from prettytable import PrettyTable
from collections import defaultdict



class Student:
    """ Student class"""

    def __init__(self, dict1, dict2):
        """ self function"""
        self.dict1 = dict1
        self.dict2 = dict2
        self.files_summary = defaultdict(str)
        self.files_summary2 = defaultdict(list)
        self. final_dict = defaultdict(list)
        self.analyze_files()


    def analyze_files(self):
        """ File analyze function. amost of the operetions are performed here"""
        try:
            file = open(self.dict1, encoding="utf8")
        except FileNotFoundError:
            raise FileNotFoundError("File does not exist or invalid file path")
        else:
            for line in file:
               a = line.split()
               self.files_summary[a[0]] += a[1]+ " " + a[2]   # Contains CWID and student name


        try:
            file = open(self.dict2, encoding="utf8")
        except FileNotFoundError:
            raise FileNotFoundError("File does not exist or invalid file path")
        else:
            for line in file:
                b = line.split()
                c = b[1] + " "+ b[2]
                self.files_summary2[b[0]].append(c)       # Contains CWID and Courses
            for key, val in self.files_summary2.items():
                val.sort()


        ds = [self.files_summary, self.files_summary2]

        for i in self.files_summary.keys():
            self.final_dict[i] = [self.files_summary[i] for self.files_summary in ds]   # merges self.files_summary and self.files_summary2


    def pretty_print(self):
        """ prints prettytable """
        pt = PrettyTable(field_names=['CWID', 'Name', 'Completed Courses'])
        for key, val in self.final_dict.items():
            pt.add_row([key,val[0],val[1]])
        print(pt)





class Instructor:
    """ Instructor class"""
    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2
        self.files_summary = defaultdict(str)
        self.files_summary2 = defaultdict(int)
        self.final_dict = defaultdict(list)
        self.analyze_files()


    def analyze_files(self):
        """ File analyze function. amost of the operetions are performed here"""
        try:
            file = open(self.dict1, encoding="utf8")
        except FileNotFoundError:
            raise FileNotFoundError("File does not exist or invalid file path")
        else:
            for line in file:
                a = line.split()
                self.files_summary[a[1] + " " + a[2]] = a[4]  # merges courses and instructor CWID
                self.files_summary2[a[1] + " " + a[2]] = self.files_summary2.get(a[1] + " " + a[2], 0) + 1  # Counts number of student in course



            ds = [self.files_summary, self.files_summary2]

            for i in self.files_summary.keys():
                self.final_dict[i] = [self.files_summary[i] for self.files_summary in ds]   # merges self.files_summary and self.files_summary2



        try:
            file = open(self.dict2, encoding="utf8")
        except FileNotFoundError:
            raise FileNotFoundError("File does not exist or invalid file path")
        else:
            for line in file:
                b = line.split()
                for k, v in self.final_dict.items():
                    if  v[0] == b[0]:
                        self.final_dict[k].append(b[1]+ ""+ b[2])   # appends instructor name
                        self.final_dict[k].append(b[3])             # appends instructor department


    def pretty_print(self):
        """ prints prettytable """
        pt = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for key, val in self.final_dict.items():
            pt.add_row([val[0],val[2],val[3],key,val[1]])
        print(pt)



def main():
    Student('D:/students.txt', 'D:/grades.txt').pretty_print()
    Instructor( 'D:/grades.txt', 'D:/instructors.txt').pretty_print()