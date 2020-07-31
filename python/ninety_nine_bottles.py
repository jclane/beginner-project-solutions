def ninety_nine_bottles():
    for i in range(99, 1, -1):
        first_line = "{} bottles of beer on the wall. ".format(str(i))
        print(first_line * 2, "\nTake one down, pass it around. {} {} of beer on the wall.".format(str(i - 1), "bottle" if (i - 1) == 1 else "bottles"))
        
ninety_nine_bottles()
