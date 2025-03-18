""" is_hot = True

if is_hot:
    print("It's is a hot day")
else:
    print("It's is a cold day") """


house_price = 10000
buyer = "Good credit"
payment = 0

if buyer == "Good credit":
    payment = house_price * 0.1
else:
    payment = house_price * 0.2  

print(f'The payment of the buyer is ${int(payment)}.')        


""" 
if name is less than 3 characters long name must be at least 3 characters otherwise if it's maore than 50 characters long name can be a maximum of 50 characters otherwise 
the name looks good...!
 """
name = (input("What is your first name? "))

if len(name) < 3:
    print("name must be at least 3 characters")

elif len(name) > 50:
    print("name can be a maximum of 50 characters")

else:
    print(f'{name} looks good...Well Done!!')