import sys
from glob import glob
from time import time
import os
import subprocess
from time import sleep

check_interval = 0.1


def main():
    python_path = sys.executable
    args = [python_path] + sys.argv[1:]
    start_time = time()
    files = get_python_files()
    for file in files:
        with open(file) as f:
            print(os.fstat(f.fileno()).st_mtime)
    child = subprocess.Popen(args)
    while True:
        sleep(check_interval)
        if child.poll() is not None:
            quit()
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
    files = glob("*.py")
    files.remove(sys.argv[0])
    return files


main()
