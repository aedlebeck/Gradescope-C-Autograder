# C/C++ Gradescope Autograder
Simple and easy to modify gradescope autograder for C/C++ files.  

## Documentation
**setup.sh**  
* Automatically installs dependencies for gradescope docker

**run_autograder.py**
* Entry point for the gradescope autograder
* This file is called when a submission is made

**run_tests.py**
* Entry point for running tests on student submission
* File is called when 

**grade_util.py**
* Contains Config of filenames and directories
* Contains helper functions for testing
* Keeps filenames/directories consistent throughout testing

**test_files.py**
* Example test case that checks if student submitted all files 


## Deployment
All of the files must be compressed into a zip with the same file heirarchy as shown in the "example.zip".  
The compressed file is then uploaded to gradescope.

**A few steps have to be taken before compressing:**

Rename "run_autograder.py" to "run_autograder":
```bash
  mv run_autograder.py run_autograder
```

Add executable access to "run_autograder":
```bash
  chmod +x run_autograder
```

