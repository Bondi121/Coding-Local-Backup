
shopping_list = []

def add_to_list(item):
    shopping_list.append(item)
    print("The item was added, there are currently ", len(shopping_list), "items in the list currently. ")



def show_list():
    print("here is your shopping list")
    for item in shopping_list:
        print(item) 

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.    
Enter 'SHOW' to see your current list.
""")

show_help()
while True:
    new_item = input("> ")

    if new_item == "DONE":
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    add_to_list(new_item)

show_list()