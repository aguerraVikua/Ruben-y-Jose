num1 = input("Please enter the number: ")

if num1.isnumeric():
    num1=int(num1)
    if num1 %2 == 0:
        print(f"The number {num1} is even")
    else:
        print(f"The number {num1} is odd")

else: 
    print("Invalid input")