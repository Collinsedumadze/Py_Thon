NUMBER =int(input("Enter your number  "))
# if the number is divisible by 3 and 5 without a reminder
if NUMBER % 3 ==0 and NUMBER % 5 == 0:
    print("FlizzBuzz") 
# if the number is divisible by 5   
elif NUMBER % 5 == 0:
    print("Buzz")
# if the number is divisible by 3     
elif NUMBER % 3 == 0:
     print("Fizz")
# if the number is not divisible by 3 and 5     
else:
    print("The number can't be found")   
