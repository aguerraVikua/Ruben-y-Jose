number = int(input("Please enter a number: "))

for number_for in range(1,number+1,2):
    if number_for+2 > number:
        print(number_for)
    else:
        print(number_for,end= ",")