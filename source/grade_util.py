from pathlib import Path

class Config:
    # Directories
    source_dir = "./source"
    submission_dir = "./submission"
    results_dir = "./results"
    test_dir = "testing"

    # Test filenames
    makefile = "/makefile"
    TestDrivercpp = ""

    # Student submission filenames
    student_source = ""
    student_header = ""

    # Answer filenames
    # Txt files containing expected STDOUT
    add_answer = ""
    remove_answer = ""
    violations_answer = ""


def read_answer(filename):
    try:
        answers = set()
        with open(filename) as file:
            for line in file.readlines():
                answers.add(line.strip())
        return answers
    except:
        print("Error unable to read answers")


def file_exists(path: str) -> bool:
    return Path(path).is_file()

