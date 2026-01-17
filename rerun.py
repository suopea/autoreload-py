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
    print(args)
    files = get_python_files()
    print(f"files are {files}")
    for file in files:
        with open(file) as f:
            print(os.fstat(f.fileno()).st_mtime)
    child = subprocess.Popen(args)
    while True:
        sleep(check_interval)
        if something_changed(files, start_time):
            child.kill()
            # todo wait for child to die
            sleep(0.2)
            child = subprocess.Popen(args)
            start_time = time()
        # todo if child quits quit the parent


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
