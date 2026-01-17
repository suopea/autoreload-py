import sys
from glob import glob
from time import time
import os
import subprocess
from time import sleep

check_interval = 0.1


def main():
    if len(sys.argv) < 2:
        print("""
    Use like this:

        autoreload.py your_script.py

    Or with arguments:

        autoreload.py your_script.py arg1 arg2

    your_script will be run and automatically reloaded
    whenever changes are detected
        """)
        quit()
    python_path = sys.executable
    args = [python_path] + sys.argv[1:]
    start_time = time()
    files = get_python_files()
    child = subprocess.Popen(args)
    while True:
        sleep(check_interval)
        if something_changed(files, start_time):
            child.kill()
            child = subprocess.Popen(args)
            start_time = time()


def something_changed(files, start_time):
    if len(get_python_files()) != len(files):
        return True
    for file in files:
        with open(file) as f:
            if os.fstat(f.fileno()).st_mtime > start_time:
                return True
    return False


def get_python_files():
    return glob("**/*.py") + glob("*.py")


main()
