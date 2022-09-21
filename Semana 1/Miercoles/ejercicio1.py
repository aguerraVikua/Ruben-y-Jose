num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")

if num1.isnumeric() and num2.isnumeric():
    num1=int(num1)
    num2=int(num2)
    if num2 == 0:
        print("Error second number can't be 0")
    else:
        print(f"The result is {num1/num2}")
else: 
    print("Invalid input")