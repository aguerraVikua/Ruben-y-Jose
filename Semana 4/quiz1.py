def main():
    products = {
        "mobiles": {
            "Apple": [
                {
                    "id": 1,
                    "name": "iPhone 7",
                    "price": 300
                },
                {
                    "id": 2,
                    "name": "iPhone 8",
                    "price": 350
                },
                {
                    "id": 3,
                    "name": "iPhone Xr",
                    "price": 450
                },
                {
                    "id": 4,
                    "name": "iPhone Xs",
                    "price": 460
                },
                {
                    "id": 5,
                    "name": "iPhone 11",
                    "price": 900
                },
                {
                    "id": 6,
                    "name": "iPhone 12",
                    "price": 1100
                },
                {
                    "id": 7,
                    "name": "iPhone 13",
                    "price": 1300
                },
            ],
            "Samsung": [
                {
                    "id": 8,
                    "name": "Samsung Galaxy Beam",
                    "price": 150
                },
                {
                    "id": 9,
                    "name": "Samsung Galaxy S6",
                    "price": 200
                },
                {
                    "id": 10,
                    "name": "Samsung Galaxy S7",
                    "price": 300
                },
            ],
            "Xiaomi": [
                {
                    "id": 11,
                    "name": "Xiaomi Redmi Note 8",
                    "price": 250
                },
                {
                    "id": 12,
                    "name": "Xiaomi Redmi Note 8 Pro",
                    "price": 300
                },
            ]
        },
        "laptops": {
            "DELL": [
                {
                    "id": 13,
                    "name": "Dell Inspiron 15",
                    "price": 600
                },
                {
                    "id": 14,
                    "name": "Dell Latitude 14",
                    "price": 650
                },
            ],
            "MAC": [
                {
                    "id": 15,
                    "name": "MacBook Pro 13",
                    "price": 900
                },
                {
                    "id": 16,
                    "name": "MacBook M1",
                    "price": 1500
                },
            ]
        },
    }

    while True:
        option = input("Please enter a valid option:\n1-Show Inventory\n2-Purchase\n3-Exit\n-->")
        if option == "1":
            for type, brands in products.items():
                for brand, product_list in brands.items():
                    for product in product_list:
                        for key, value in product.items():
                            if key == "price":
                                print(value)
                            else:
                                print(value,end = "-")
        elif option == "2":
            product_id = int(input("Please enter the product id: "))
            product_selected = None
            client = {}
            for type, brands in products.items():
                for brand, product_list in brands.items():
                    for product in product_list:
                        if product.get("id") == product_id:
                            product_selected = product
                            break
            if product_selected == None:
                print("Product not found")
                continue
            else :
                client["name"] = input("Please enter your name: ")
                client["lastname"] = input("Please enter your lastname: ")
                client["id_card"] = input("Please enter your id card: ")
                client["product_id"] = product_id

            print("***** RECEIPT ******")
            print("Name:",client.get("name"))
            print("Lastname:",client.get("lastname"))
            print("Id Card:",client.get("id_card"))
            print("Product:",product_selected.get("name"))
            print("Total:",product_selected.get("price"))

        elif option == "3":
            break
        else:
            continue

main()

