num1 = int(input("Enter the first number = "))
num2 = int(input("Enter the second number = "))
ope = input("Enter the operators for calculation (+,-,*,/) = ")

if (ope == '+'):
    print(int(num1)+int(num2))
elif (ope == '-'):
    print(int(num1)-int(num2))
elif(ope == '*'):
    print(int(num1)*int(num2))
elif(ope == '/'):
    print(int(num1)/int(num2))
else:
    print("You enter the Invaild operators!")

