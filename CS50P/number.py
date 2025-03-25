def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            #print("x is not a number")
            # what if you want to silently ignore
            pass


main()