"""
def main():
    name = get_name()
    house = get_house()
    print(f"{name} lives in {house}")


def get_name():
    return input("Name: ")  


def get_house():
    return input("House: ")  


if __name__ =="__main__":
    main()


#Using unpacking method

def main():
    name, house = student()
    print(f"{name} lives in {house}")


def student():
    return input("Name: "), input("House: ") 
 


if __name__ =="__main__":
    main()

      

#Using Tuple and List method but the difference is their mutability

def main():
    student = Student()
    print(type(student))
    print(f"{student[0]} lives in {student[1]}")


def Student():
    return input("Name: "), input("House: ") 


if __name__ =="__main__":
    main()


#Using Tuple and List method but the difference is their mutability

def main():
    student = Student()
    print(type(student))
    print( 
    f"{student[0]} lives in {student[1]}")


def Student():
    return input("Name: "), input("House: ") 


if __name__ =="__main__":
    main()
"""

for i in range(0,10):
    print(i )
print('end')