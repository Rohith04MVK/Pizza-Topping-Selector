import requests
from termcolor import colored
pizza = ["Margherita", "Pepperoni Feast", "Veggie Supreme", "Ultimate chicken", "Original Pan"]
toppings = ["Pepperoni", "Cheese", "Tomatoes", "Brocol", "Bacon", "Chilliflakes"]
toppings_list = []
toppings_price_list = []
toppings_price = {"Pepperoni": 28, "Cheese": 28, "Tomatoes": 28, "Brocol": 28, "Bacon": 28, "Chilliflakes": 0}
price = {"Margherita": "280", "Pepperoni Feast": "290", "Veggie Supreme": "340", "Ultimate chicken": "305", "Original Pan": "210" }
pincode = input('Enter your pincode: ')
url = (f'https://api.postalpincode.in/pincode/{pincode}')
def get_pincode():
    response = requests.get(url, headers={"Accept": "application/json"})
    data = response.json()
    Name = (data[0]['PostOffice'][0]['Name'])
    return Name                                                                                                                                                   
def bill():
    for r in toppings_list:
        f = toppings_price.get(r)
        toppings_price_list.append(f)
        toppings_total = sum(toppings_price_list)
        bill = (int(price.get(order_pizza))) + (toppings_total)
        return (str(bill) +" ₹")  
print(f"Welcome to {get_pincode()} Pizza Hut")
print("These Are the pizza that is available:")
for i in pizza:
    print(i)
order_pizza = input("Which Pizza would you like:")
if order_pizza not in pizza:
    print("Invalid entry") 
else:
    num_toppings = int(input("How many toppings would you like: "))
    if num_toppings == 0:
        print("No toppings where added to your pizza")
        print(price.get(order_pizza) +" ₹") 
    elif num_toppings > 4:
        print("Max number of toppings is 4")
    else:
        print("These are the toppings available")
        for f in toppings:
            print(f)
        for l in range(1, num_toppings+1):
            order_toppings = str(input("Which toppings would you like to add: "))
            toppings_list.append(order_toppings)
        print(f"The pizza you ordered is: {order_pizza}")
        print("These are the toppings you ordered:")
        print(toppings_list)
        conformation = str(input("Is this the pizza you would like to order y/n:"))
        if conformation == "n":
            print("You have cancled the order.")
        else:
            print(bill())