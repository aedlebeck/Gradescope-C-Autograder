import unittest
import subprocess
from gradescope_utils.autograder_utils.decorators import weight, number, visibility


class TestCompilation(unittest.TestCase):
    @weight(20)
    @number("1")
    @visibility("visisble")
    def test_compilation(self):
        """Compilation Check"""
        try:
            make_process = subprocess.run("make", cwd='testing', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            return_code = make_process.returncode

            self.assertEqual(return_code, 0)
            if return_code == 0:
                print("Program successfully compiles")
                return True
            else:
                print("Make Error Code: ", return_code)
                print(make_process.stderr.decode('utf-8'))
                print(make_process.stdout.decode('utf-8'))
                return False
        except:
            print("Make Error Code: ", return_code)
            print(make_process.stderr.decode('utf-8'))
            self.assertEqual(return_code, 0)