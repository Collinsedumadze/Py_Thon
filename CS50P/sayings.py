def main():
    hello("world")
    goodbye("world")

def hello(name):
    print("hello,", name)


def goodbye(name):
    print("goodbye,", name)

#this is a way to run the main function so that in case it is imported, doesnt print out everything but the one specified by the user

if __name__ == "__main__":
    main()

