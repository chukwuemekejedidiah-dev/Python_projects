inventory = ["laptop", "keyboard", "mouse", "monitor"]
item = input("Enter an item to check if it's in the inventory:  ")

def check_item(item):
    for i in range(len(inventory)):
       if inventory[i] == item:
            print(f"{item} found in inventory!")
            return
    print(f"{item} not found in inventory.")    
           
check_item(item)