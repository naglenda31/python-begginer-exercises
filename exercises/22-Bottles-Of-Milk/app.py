verse1 = "bottles of milk on the wall"
verse2 = "Take one down and pass it around, "
verse3 = "bottles of milk."

def number_of_bottles():
    for i in reversed(range(100)):
        if i == 2:
            print(str(i) + " " + verse1 + ", " + str(i) + " " + verse3 + "\n" 
            + verse2 + str(i-1) + " " + "bottle of milk on the wall.")
        elif i == 1:
            print(str(i) + " bottle of milk on the wall, " + str(i) + " bottle of milk." + "\n" + "Take one down and pass it around, no more bottles of milk on the wall.")
        elif i == 0:
             print("No more bottles of milk on the wall, no more bottles of milk. \nGo to the store and buy some more, 99 bottles of milk on the wall.\n")
        else:
            print(str(i) + " " + verse1 + ", " + str(i) + " " + verse3 + "\n"
            + verse2 + str(i-1) + " " + "bottles of milk on the wall.")

    

number_of_bottles()