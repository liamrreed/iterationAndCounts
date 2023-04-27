current_order = []    # purpose is to track all items in the current customer's order
all_customers = []    # initialize a list to an empty list
running = True        # will allow ordering loop to run until running is set to false

while running:
    current_order.append("beef")
    current_order.append("pepsi")
    current_order.append("medium")
    current_order.append(3)

    all_customers.append(current_order) # [['beef', 'pepsi', 'medium', '3']
    current_order = []
    running = bool(int(input("Would you like to place another? 1 or 0")))
    # assume user enter a 1

for customer in all_customers:
    print(f"You ordered a {customer[0]}, to drink a {customer[1]}" + 
         f" and a {customer[2]} fries, and {customer[3]} ketchup.")
