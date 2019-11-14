from HW11_Ameya_Desai import Repository
import unittest



class TestContainer(unittest.TestCase):
    # unittest class

    def test_Repository(self):
        """Tests Class repository"""
        F1 = Repository('D:/majors_11.txt', 'D:/students_11.txt', 'D:/grades_11.txt', 'D:/instructors_11.txt')

        a1 = [['SFEN', [['SSW 540', 'SSW 810', 'SSW 555'], ['CS 501', 'CS 546']]], ['CS', [['CS 570', 'CS 546'], ['SSW 810', 'SSW 565']]]]
        a2 = [[k, v] for k, v in F1.majors_summery_dict.items()]

        b1 = [['10103', ['Jobs, S', 'SFEN', ['SSW 810', 'CS 501'], ['SSW 540', 'SSW 555'], [None]]], ['10115', ['Bezos, J', 'SFEN', ['SSW 810'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546']]], ['10183', ['Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546']]], ['11714', ['Gates, B', 'CS', ['SSW 810', 'CS 546', 'CS 570'], [], [None]]]]
        b2 = [[k, v] for k, v in F1.student_summery_dict.items()]

        c1 = [[('SSW 810', '98763'), ['98763', 4, 'Rowland, J', 'SFEN']], [('CS 501', '98762'), ['98762', 1, 'Hawking, S', 'CS']], [('CS 546', '98762'), ['98762', 1, 'Hawking, S', 'CS']], [('SSW 555', '98763'), ['98763', 1, 'Rowland, J', 'SFEN']], [('CS 546', '98764'), ['98764', 1, 'Cohen, R', 'SFEN']], [('CS 570', '98762'), ['98762', 1, 'Hawking, S', 'CS']]]
        c2 = [[k,v] for k, v in F1.instructor_summery_dict.items()]

        self.assertEqual(a1, a2)
        self.assertEqual(b1, b2)
        self.assertEqual(c1, c2)




if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)