def main():
    x = int(input("What is x? "))
    print("x is", squared(x))


def squared(x):
    return x * x


if __name__ == "__main__":
    main()