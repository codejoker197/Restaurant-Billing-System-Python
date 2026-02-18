# Define the menu of restaurant
menu = {
    'Pizza' : 40,
    'Pasta' : 20,
    'Burger': 60,
    'French_fries' : 65,
    'Cold_drink': 25,
    'Coffee': 80,   
}

# Greet
print("Welcome to Shiv Restaurant")
print(" Pizza : Rs-40\n Pasta : Rs-20\n Burger : Rs-60\n French_fries : Rs-65 \n Cold_drink : Rs-25\n Coffee : Rs-80")

Order_Total=0
# 80+20=100
item_1 = input("Enter the name of menu you want to order ->")
if item_1 in menu:
    Order_Total += menu[item_1]
    print(f"Your item {item_1} added to your order")
    
else:
    print(f"ordered item {item_1} is not avaialable yet")

another_order = input("Do you want to add another item ? (Yes/No)-> ")
if another_order == "yes":
    item_2 = input("Enter the name of second order ->")
    if item_2 in menu:
        Order_Total += menu [item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"orderd item {item_2} is not avaialabel!")  
        
print(f"The total amount of item to pay is : {Order_Total}") 
