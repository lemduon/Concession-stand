## MENU ##
# Configure if you want #
menu = {
    "pizza": 4.99,
    "nachos":2.99,
    "popcorn":1.99,
    "soda":0.99,
    "corn dog":1.49,
    "hot dog":1.49
}
cart = []
total = 0
### MENU PRINTING ###
print("______________________________________________________________")
print("-----------------------------MENU-----------------------------")

items = menu.items()
for key, value in items:
    print(f"{key}: ${value}.")

while True:
    food = input("Type in what you want to order (q to quit): ").lower()
    if food == 'q':
        break
    else:
        if menu.get(food) is not None:
            cart.append(food)
print(cart)

for food in cart:
    total += menu.get(food)

print(f"Your total is ${total}")

# Does allow duplicates if you're wondering

