age = int(input("Enter your age = "))

if age >= 18:
    print("you are greater than 18")
    print("you can vote")
elif age>=3 and age<18:
    print("you are in school age")
    print("you can't vote")
else:
    print("you are kid")
print("THANK YOU!")