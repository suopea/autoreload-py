import sys
from glob import glob
from time import time
import os
import subprocess
from time import sleep

check_interval = 0.1


class Project:

    def __init__(self):
        self.type = None
        self.auto_args = True
        self.files = []
        self.args = []

    def update_files(self):
        if self.type == "py":
            self.files = get_python_files()
        elif self.type == "c":
            self.files = get_c_files()

    def detect_type(self):
        if get_python_files() != []:
            self.type = "py"
        elif get_c_files() != []:
            self.type = "c"
        else:
            self.type = None

    def wait_for_first_file(self):
        while self.type is None:
            sleep(check_interval)
            self.detect_type()

    def update_args(self):
        pass


def main():
    files = get_python_files()
    if len(sys.argv) < 2:
        if len(files) > 1:
            print_info()
            quit()
        elif len(files) == 0:
            print("No arguments and no .py files found.")
            wait_for_a_script_to_be_created()
        args = [sys.executable, get_python_files()[0]]
    else:
        args = [sys.executable] + sys.argv[1:]
    start_time = time()
    files = get_python_files()
    child = subprocess.Popen(args)
    while True:
        sleep(check_interval)
        if something_changed(files, start_time):
            child.kill()
            if get_python_files() == []:
                wait_for_a_script_to_be_created()
                args = [sys.executable, get_python_files()[0]]
            child = subprocess.Popen(args)
            start_time = time()


def get_python_files():
    return glob("**/*.py", recursive=True)


def get_c_files():
    files = glob("**/*.c", recursive=True)
    files += glob("**/*.h", recursive=True)
    files += glob("*akefile")
    return files


def print_info():
    print("""
    More than one .py file found

    Use like this:

        /path/to/autoreload.py your_script.py

    Or with arguments:

        /path/to/autoreload.py your_script.py arg1 arg2

    your_script will be run and automatically reloaded
    whenever changes are detected
        """)


def wait_for_a_script_to_be_created():
    print("\n  waiting for a .py file to be created...\n")
    while get_python_files() == []:
        sleep(check_interval)


def something_changed(files, start_time):
    if len(get_python_files()) != len(files):
        return True
    for file in files:
        with open(file) as f:
            if os.fstat(f.fileno()).st_mtime > start_time:
                return True
    return False

    main()
