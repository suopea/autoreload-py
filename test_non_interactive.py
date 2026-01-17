import sys

for arg in sys.argv[1:]:
    print(arg, "in reverse is", arg[::-1])
