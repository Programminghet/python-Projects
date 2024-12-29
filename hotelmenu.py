#restaurant menu 
menu = {
    'Pizza' : 400,
    'Pasta' : 450,
    'Burger' : 300,
    'French fries' : 100,
    'Dosa' : 100,
    'Salad' : 800,
    
}

print ("Welcome to Our Restaurant")
print ("Pizza: 400\nPasta: 450\nBurger: 300\nfrench fries: 100\nDosa: 100\nSalad: 800")

order_total = 0 

item_1 = input("Enter the item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your order {item_1} has been added")
else:
    print(f"ordered {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No)  ")
if another_order == "Yes":
 item_2 = input("Enter the name of second item =")
 if item_2 in menu:
   order_total += menu[item_2]
   print(f"Your order {item_2} has been added")
 else:
    print(f"Ordered item  {item_2}  is not available yet!")

print(f"Total amount to pay {order_total}") 



