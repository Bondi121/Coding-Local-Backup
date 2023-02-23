SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100  

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE + SERVICE_CHARGE)
while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    user_name = input("What's your username?")
    try:
        ticket_number = int(input("How many tickets do you like, {}? " .format(user_name)))
        if ticket_number > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {} Please try again.".format(err))
    else:
        price = calculate_price(ticket_number)
        print("The price is", price)
        user_continue = str(input("Would you like to continue, Y/N?"))
        if user_continue.lower() == "y":
            print("SOLD!")
            tickets_remaining -= ticket_number
        else:
            print("Thanks {} " .format(user_name))
print("sorry the tickets are sold out")