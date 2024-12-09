def quantity_prompt():
    while True:
        try:
            quantity = int(input("\nHow many tickets would you like to purchase? "))
            if quantity > 0:
                return quantity
            print("Invalid input. Please enter a whole positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def ticket_purchase():
    locations = {
            '1': ("London", 10.15),
            '2': ("Bermingham", 22.50),
            '3': ("Manchester", 21.40)
        }
    
    while True:
        print("\nWhere are you travelling to?\n ")
        for key, (location, price) in locations.items():
            print(f"{key} - {location} (£{price:.2f})")
        choice = input("\nPlease enter your choice (1-3): ")
        if choice in locations:
            return choice, locations[choice]
        print("Invalid choice. Please try again.")    

def main():
    name = input("\nPlease enter lead passenger name: ")

    choice, (location, price) = ticket_purchase()
    quantity = quantity_prompt()
    cost = price * quantity 
    print(f"\n{name}, \nYou have chosen {quantity} ticket(s) to {location}.\nTotal cost: {quantity} x £{price} = £{cost:.2f}")
    
    
    receipt_prompt = input("Would you like to print your receipt? (yes/no)").lower()
    if receipt_prompt == 'yes': 
        receit_name = name + '.txt'   
        receipt = open(receit_name, "w")
        receipt.write(f"Receipt of ticket purchase\n\nName of customer: {name}\n\nDestination: {location}\n\nQuantity: {quantity}\n\nThank you for your custom!")
        receipt.close()

    elif receipt_prompt == 'no':    
        print("thank you!")    
           
    else:    
        print("Invalid choice, please try again")        

    

main()