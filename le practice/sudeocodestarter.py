#Jc 2nd starter suedocode

board_list1 = ["","",""]
board_list2 = ["","",""]
board_list3 = ["","",""]
if board_list1.index(1) == "O" and board_list2.index(2) == "O" and board_list3.index(3) == "O":
    print("You lose")
if board_list3.index(1) == "O" and board_list2.index(2) == "O" and board_list1.index(3) == "O":
    print("You lose")
if board_list1.index(1) == "O" and board_list2.index(1) == "O" and board_list3.index(1) == "O":
    print("You lose")
if board_list1.index(2) == "O" and board_list2.index(2) == "O" and board_list3.index(2) == "O":
    print("You lose")
if board_list1.index(3) == "O" and board_list2.index(3) == "O" and board_list3.index(3) == "O":
    print("You lose")