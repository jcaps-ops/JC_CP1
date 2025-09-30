#JC 2nd shopping list manager
shoppinglist = []
while True:
    action = input("Would you like to add or remove something from your shopping list (Type add or remove) type exit to leave or type show to show the list:")
    #Write your code here
    if action == "add":
        adding = input("What would you like to add:")
        shoppinglist.append(adding)
    if action == "remove":
        removing = input("What do yo want to remove:")
        shoppinglist.remove(removing)
        
    if action == "exit":
        break
    if action == "show":
        print(shoppinglist)