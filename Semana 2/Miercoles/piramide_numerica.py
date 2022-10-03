number = int(input("Please enter a number:"))
#aux = 1
#aux2 = 1

for i in range(0,number):
    for j in range(2*i+1,0,-2):
        if j == 1:
            print(j)
        else:
            print(j, end=" ")

"""
while aux <= number:
    aux3 = aux2
    while aux3 >= 1:
        if aux3 == 1:
            print(aux3)
        else:
            print(aux3, end=" ")
        aux3-=2
    aux2+=2
    aux+=1
    
"""