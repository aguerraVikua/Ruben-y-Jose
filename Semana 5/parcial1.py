def isPrime(last_rif):
    number = int(last_rif)
    aux = number -1
    while aux > 1:
        if number%aux == 0:
            return False
        aux -=1
    return True

def main():
    products = {
        "Q":{
            "description":"Quimico",
            "price": 1000
        },
        "F":{
            "description":"Farmaceutico",
            "price": 2500
        },
        "B":{
            "description":"Biologico",
            "price": 4000
        }
    }
    print(" ***** WELCOME TO SAMAN INTERNACIONAL *****")
    customer_f =0    
    customer_q =0    
    customer_b =0
    discount_f =0    
    discount_q =0    
    discount_b =0  
    total_day = 0
    rif_max_purchase = 0 
    max_purchase = 0 
    while True:
        rif = input("Please enter your rif:\n->")
        product_purchase = input("Please enter the product do you want: \nQ-Quimico\nF-Farmaceutico\nB-Biologico\n->")
        payment_method = input("Please enter the payment method: \nC-One time payment\nR-Credit\n->")
        subtotal = products.get(product_purchase).get("price")
        discount =0
        recharge = 0
        tax = 0
        #Descuentos
        if payment_method == "C":
            discount += subtotal * 0.03
        if subtotal %2 ==0:
            discount += subtotal * 0.02
        if isPrime(rif[len(rif)-1]):
            discount += subtotal * 0.05
        #Recargos
        if payment_method == "R":
            recharge += subtotal * 0.1
        
        gross_amount = subtotal+ recharge - discount

        if product_purchase == "Q" or product_purchase == "B":
            tax += gross_amount * 0.12 
    
        net_amount = gross_amount + tax

        if product_purchase == "F":
            customer_f +=1
            discount_f += discount
        elif product_purchase == "Q":
            customer_q +=1
            discount_q += discount
        elif product_purchase == "B":
            customer_b +=1
            discount_b += discount
        
        total_day += net_amount

        if net_amount > max_purchase:
            max_purchase = net_amount
            rif_max_purchase =rif
        
        print("****** INVOICE *******")
        print("Rif:",rif)
        print("Product Line:", products.get(product_purchase).get("description"))
        print("Payment method:",payment_method)
        print("Discount:",discount)
        print("Tax:",tax)
        print("Total:",net_amount)

        if input("Do you want to exit: Y-Yes or N-No") == "Y":
            break
    print("****** END OF DAY *******")
    print("Customer F:",customer_f)
    print("Customer B:",customer_b)
    print("Customer Q:",customer_q)
    print("Discount F:",discount_f)
    print("Discount Q:",discount_q)
    print("Discount B:",discount_b)
    print("Rif Max Purchase:",rif_max_purchase)
    print("Total day:",total_day)
    



main()