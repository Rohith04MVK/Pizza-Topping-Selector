import requests
pizza = ["Margherita", "Pepperoni Feast", "Veggie Supreme", "Ultimate chicken", "Original Pan"]
toppings = ["Pepperoni", "Cheese", "Tomatoes", "Brocol", "Bacon", "Chilliflakes"]
toppings_list = []
toppings_price_list = []
toppings_price = {"Pepperoni": 28, "Cheese": 28, "Tomatoes": 28, "Brocol": 28, "Bacon": 28, "Chilliflakes": 0}
price = {"Margherita": "280", "Pepperoni Feast": "290", "Veggie Supreme": "340", "Ultimate chicken": "305", "Original Pan": "210" }

pincode = input('Enter your Pincode: ')
url = (f"https://api.postalpincode.in/pincode/{pincode}")
response = requests.get(url, headers={"Accept": "application/json"})
data_json = response.json()
for data in data_json:
    unpacked_data = (data)
refined_data = (unpacked_data['PostOffice'])
for datas in refined_data:
    final_data = (datas)
Name = (final_data['Name'])
print(f'Welcome to {Name} Pizza Hut')

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
            for r in toppings_list:
                f = toppings_price.get(r)
                toppings_price_list.append(f)
            toppings_total = sum(toppings_price_list)            
            print("The bill be given in a few moments.")
            bill = (int(price.get(order_pizza))) + (toppings_total)
            print(str(bill) +" ₹")
    print(f"Thank you for visiting {Name} Pizza Hut")