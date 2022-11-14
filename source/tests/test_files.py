import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from gradescope_utils.autograder_utils.files import check_submitted_files


class TestFiles(unittest.TestCase):
    @weight(0)
    @number("0")
    @visibility("visisble")
    def test_submitted_files(self):
        """Submitted Files Check"""
        try:
            missing_files = check_submitted_files(['RedBlackTree.cpp', 'RedBlackTree.h'], base='submission')
            for path in missing_files:
                print('Missing {0}'.format(path))
            self.assertEqual(len(missing_files), 0, 'Missing some required files!')
            print('All required files submitted!')
        except:
            print("Error testing for submitted files")