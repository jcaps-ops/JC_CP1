#JC 2nd shopping list manager
shoppinglist = []
while True:
    action = input("Would you like to add or remove something from your shopping list (Type add or remove) type exit to leave or type show to show the list:")
    #Write your code here
    if action == "add":
        adding = input("What would you like to add:")
        shoppinglist.append(adding)
    elif action == "remove":
        removing = input("What do yo want to remove:")
        if removing in shoppinglist:
            shoppinglist.remove(removing)
        else:
            print("That is not one of the items")
        
    elif action == "exit":
        break
    elif action == "show":
        print(shoppinglist)
    else:
        print("That is not an acepted answer")
        