number = int(input("Please enter a number: "))
aux = number-1
is_prime = True

while aux > 1:
    print("aux",aux)
    print("operation",number%aux)
    if number%aux == 0:
        print("entre en el if")
        is_prime = False
        break
    aux-=1

if is_prime:
    print(f"The number {number} is prime")
else:
    print(f"The number {number} is not prime")
    