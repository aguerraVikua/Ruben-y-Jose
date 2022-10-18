pd = {}
while True:
    key =  input("What type of data do you want to add: ")
    value = input("What is the value: ")

    pd[key] = value

    for key_to_print,value_to_print in pd.items():
        print(f"Your {key_to_print} is {value_to_print}")
    
    if input("Do you want to exit: \nY-Yes\nN-No\n->") == "Y":
        break
    