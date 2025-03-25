import sys

if len(sys.argv) < 2:
    print("Too few arguments")

    # Intro to slicing e.g [1:8]

    for arg in sys.argv[1:]:
        print(arg)

        
    print("hell0, my name is", arg)
""" elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hell0, my name is", sys.argv[1]) """