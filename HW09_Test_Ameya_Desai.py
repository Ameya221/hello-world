from HW09_Ameya_Desai  import Student, Instructor
import unittest


class TestContainer(unittest.TestCase):
    # unittest class
    def test_Student(self):
        """Tests Class Student"""
        F1 = Student('D:/students.txt', 'D:/grades.txt')
        a = [['10103', ['Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']]], ['10115', ['Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']]], ['10172', ['Forbes, I', ['SSW 555', 'SSW 567']]], ['10175', ['Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']]], ['10183', ['Chapman, O', ['SSW 689']]], ['11399', ['Cordova, I', ['SSW 540']]], ['11461', ['Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']]], ['11658', ['Kelly, P', ['SSW 540']]], ['11714', ['Morton, A', ['SYS 611', 'SYS 645']]], ['11788', ['Fuller, E', ['SSW 540']]]]
        b = [[k,v] for k, v in F1.final_dict.items()]
        self.assertEqual(a, b)

        with self.assertRaises(FileNotFoundError):
            Student('D:/tudents.txt', 'D:/grades.txt')

        with self.assertRaises(FileNotFoundError):
            Student('D:/students.txt', 'D:/rades.txt')

        with self.assertRaises(FileNotFoundError):
            Student('D:/tudents.txt', 'D:/rades.txt')


    def test_Instructor(self):
        """Tests Class Instructor"""
        F2 = Instructor( 'D:/grades.txt', 'D:/instructors.txt')
        c = [['SSW 567', ['98765', 4, 'Einstein,A', 'SFEN']], ['SSW 564', ['98764', 3, 'Feynman,R', 'SFEN']], ['SSW 687', ['98764', 3, 'Feynman,R', 'SFEN']], ['CS 501', ['98764', 1, 'Feynman,R', 'SFEN']], ['CS 545', ['98764', 1, 'Feynman,R', 'SFEN']], ['SSW 555', ['98763', 1, 'Newton,I', 'SFEN']], ['SSW 689', ['98763', 1, 'Newton,I', 'SFEN']], ['SSW 540', ['98765', 3, 'Einstein,A', 'SFEN']], ['SYS 800', ['98760', 1, 'Darwin,C', 'SYEN']], ['SYS 750', ['98760', 1, 'Darwin,C', 'SYEN']], ['SYS 611', ['98760', 2, 'Darwin,C', 'SYEN']], ['SYS 645', ['98760', 1, 'Darwin,C', 'SYEN']]]
        d = [[k,v] for k, v in F2.final_dict.items()]
        self.assertEqual(c, d)

        with self.assertRaises(FileNotFoundError):
            Student('D:/rades.txt', 'D:/instructors.txt')

        with self.assertRaises(FileNotFoundError):
            Student('D:/grades.txt', 'D:/nstructors.txt')

        with self.assertRaises(FileNotFoundError):
            Student('D:/rades.txt', 'D:/nstructors.txt')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)