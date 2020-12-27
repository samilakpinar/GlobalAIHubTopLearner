name = input("Please enter your name: ")
surname = input("Plesa enter your surname: ")
age = int(input("Please enter your age: "))
date = int(input("Please enter your date of birth(just year): "))

person = [name,surname,age,date]

for i in person:
    print(i)



if age < 18:
    print("You can't go out because it's too dangerous")
elif age >= 18:
    print("You can out to the street")
