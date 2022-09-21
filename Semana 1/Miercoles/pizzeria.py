option= int(input("Please enter a valid option: \n1-Vegetarian\n2-Non Vegetarian\n->"))
if option == 1:
    ingredient= int(input("Please enter an ingredient: \n1-Pimiento\n2-Tofu\n->"))
    if ingredient == 1:
        ingredient="Pimiento"
    else:
        ingredient="Tofu"
    print(f"The pizza ordered was Vegetarian with Tomate, Mozzarella and {ingredient}")
elif option == 2:
    ingredient= int(input("Please enter an ingredient: \n1-Peperoni\n2-Jamon\n3-Salmon\n->"))
    if ingredient == 1:
        ingredient="Peperoni"
    elif ingredient == 2:
        ingredient="Jamon"
    else:
        ingredient="Salmon"
    print(f"The pizza ordered was Non Vegetarian with Tomate, Mozzarella and {ingredient}")
else:
    print("Invalid option")
