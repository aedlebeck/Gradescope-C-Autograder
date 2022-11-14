#!/usr/bin/env python3
import os
import shutil
import subprocess
from source.grade_util import Config


# Current working directory
cwd = os.getcwd()


# Create testing directory and copy test driver files
def copy_test_files():
    try:
        # Create directory for testing student submission
        if not os.path.isdir(Config.test_dir):
            os.makedirs(Config.test_dir)

        # Copy test driver Files to test_dir
        shutil.copy2(Config.source_dir + Config.makefile, Config.test_dir)
        shutil.copy2(Config.source_dir + Config.TestDrivercpp, Config.test_dir)
    except:
        print("Error copying test files")


# Copy student Files
def copy_submission():
    try:
        if os.path.exists(Config.submission_dir + Config.student_source):
            shutil.copy2(Config.submission_dir + Config.student_source, Config.test_dir)
        else:
            print(Config.student_source, " does not exist in ", Config.submission_dir)
        if os.path.exists(Config.submission_dir + Config.student_header):
            shutil.copy2(Config.submission_dir + Config.student_header, Config.test_dir)
            return True
        else:
            print(Config.student_header, " does not exist in ",Config.submission_dir)
            return False
    except:
        print("Error copying submission files")
        return False


def make():
    try:
        make_process = subprocess.run('make', cwd=Config.test_dir, timeout=5)
    except:
        print("Error when calling make")
              

def make_clean():
    try:
        lean_process = subprocess.run("make clean", cwd=Config.test_dir, shell=True)
    except:
        print("Error when calling make clean")


if __name__ == '__main__':
    copy_test_files()
    copy_submission()
    make()
    run_tests = subprocess.run("python3 source/run_tests.py", shell=True)
    make_clean()

