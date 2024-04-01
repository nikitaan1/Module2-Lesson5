
#Task 1

def shopping_list(items_list):
    return items_list

total_items = []

while True:
    add_item = input("Add items to the cart or (when finished 'enter' done): ").lower()
    if add_item == "done":
        break
    total_items.append(add_item)

print(shopping_list(total_items))


#Task 2

def shopping_list(items_list):
    return items_list

total_items = []

while True:
    add_item = input("Add items to the cart or (when finished 'enter' done): ").lower()
    if add_item == "done":
        break
    total_items.append(add_item)

while True:
    remove_item = input("Would you like to remove some of the items? (Enter item name or 'done' to finish): ").lower()
    if remove_item == "done":
        break
    if remove_item in total_items:
        total_items.remove(remove_item)
    else:
        print("Item not found in the list.")

    print(shopping_list(total_items))

    #Task 3

def shopping_list(items_list):
    return f"Final Shopping List: {items_list}"

total_items = []

while True:
    add_item = input("Add items to the cart or (when finished, enter 'done'): ").lower()
    if add_item == "done":
        break
    total_items.append(add_item)


while True:

    if total_items: 
        remove_item = input("Would you like to remove some of the items? (Enter item name or 'done' to finish): ").lower()
        if remove_item == "done":
            break
        if remove_item in total_items:
            total_items.remove(remove_item)
        else:
            print("Item not found in the list.")
    else:  
        print("Your shopping list is empty.")
        break

print(shopping_list(total_items))