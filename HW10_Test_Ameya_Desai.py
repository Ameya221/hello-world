from HW10_Ameya_Desai import Student, Summery, Instructor
import unittest


class TestContainer(unittest.TestCase):
    # unittest class
    def test_Student(self):
        """Tests Class Student"""
        F1 = Student('D:/majors.txt')
        a = [['SFEN', [['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']]], ['SYEN', [['SYS 671', 'SYS 612', 'SYS 800'], ['SSW 810', 'SSW 565', 'SSW 540']]]]
        b = [[k,v] for k, v in F1.dfinal.items()]
        self.assertEqual(a, b)

        with self.assertRaises(FileNotFoundError):
            Student('D:/mors.txt')



    def test_Summery(self):
        """Tests Class Summery"""
        F2 = Summery('D:/student.txt', 'D:/course.txt', 'D:/majors.txt')
        a = [['10103', ['Baldwin, C', 'SFEN', ['SSW 567', 'SSW 564', 'SSW 687', 'CS 501'], ['SSW 540', 'SSW 555'], [None]]], ['10115', ['Wyatt, X', 'SFEN', ['SSW 567', 'SSW 564', 'SSW 687', 'CS 545'], ['SSW 540', 'SSW 555'], [None]]], ['10172', ['Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545']]], ['10175', ['Erickson, D', 'SFEN', ['SSW 567', 'SSW 564', 'SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545']]], ['10183', ['Chapman, O', 'SFEN', ['SSW 689'], ['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']]], ['11399', ['Cordova, I', 'SYEN', ['SSW 540'], ['SYS 671', 'SYS 612', 'SYS 800'], [None]]], ['11461', ['Wright, U', 'SYEN', ['SYS 800', 'SYS 750', 'SYS 611'], ['SYS 671', 'SYS 612'], ['SSW 810', 'SSW 565', 'SSW 540']]], ['11658', ['Kelly, P', 'SYEN', [], ['SYS 671', 'SYS 612', 'SYS 800'], ['SSW 810', 'SSW 565', 'SSW 540']]], ['11714', ['Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 671', 'SYS 612', 'SYS 800'], ['SSW 810', 'SSW 565', 'SSW 540']]], ['11788', ['Fuller, E', 'SYEN', ['SSW 540'], ['SYS 671', 'SYS 612', 'SYS 800'], [None]]]]
        b = [[k,v] for k, v in F2.dfinal.items()]
        self.assertEqual(a, b)

        with self.assertRaises(FileNotFoundError):
            Summery('D:/tudent.txt', 'D:/course.txt', 'D:/majors.txt')

        with self.assertRaises(FileNotFoundError):
            Summery('D:/student.txt', 'D:/crse.txt', 'D:/majors.txt')

        with self.assertRaises(FileNotFoundError):
            Summery('D:/student.txt', 'D:/course.txt', 'D:/maors.txt')


    def test_Instructor(self):
        """Tests Class Instructor"""
        F3 = Instructor( 'D:/course.txt', 'D:/instructor.txt')
        a = [['SSW 567', ['98765', 4, 'Einstein, A', 'SFEN']], ['SSW 564', ['98764', 3, 'Feynman, R', 'SFEN']], ['SSW 687', ['98764', 3, 'Feynman, R', 'SFEN']], ['CS 501', ['98764', 1, 'Feynman, R', 'SFEN']], ['CS 545', ['98764', 1, 'Feynman, R', 'SFEN']], ['SSW 555', ['98763', 1, 'Newton, I', 'SFEN']], ['SSW 689', ['98763', 1, 'Newton, I', 'SFEN']], ['SSW 540', ['98765', 3, 'Einstein, A', 'SFEN']], ['SYS 800', ['98760', 1, 'Darwin, C', 'SYEN']], ['SYS 750', ['98760', 1, 'Darwin, C', 'SYEN']], ['SYS 611', ['98760', 2, 'Darwin, C', 'SYEN']], ['SYS 645', ['98760', 1, 'Darwin, C', 'SYEN']]]

        b = [[k, v] for k, v in F3.dfinal.items()]
        self.assertEqual(a, b)

        with self.assertRaises(FileNotFoundError):
            Instructor('D:/ourse.txt', 'D:/instructor.txt')

        with self.assertRaises(FileNotFoundError):
            Instructor('D:/course.txt', 'D:/nstructor.txt')

        with self.assertRaises(FileNotFoundError):
            Instructor('D:/ourse.txt', 'D:/nstructor.txt')



if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)