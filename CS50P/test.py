from calculs import squared


def main():
    test_squared()


def test_squared():
    if squared(3) == 4:
        print("Test 1: OK")


if __name__ == "__main__":
    main()