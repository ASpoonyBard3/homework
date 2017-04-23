# Doesn't calculate 
bizz = 0 # create var to iterate over in while loop
while bizz < 101: # start while loop, it needs to stop after 100, not at 100, so set to 101.
#def multiple of 3
    if (bizz % 3) == 0: #if bizz is equal to 0, then using mods to compare bizz to 3 to determine multiple, remember it's equals (==) 0 not different (!=)to 0
        print ("Buzz") 
        bizz = bizz +1 #iterate + 1 to bizz, if statement terminates
    elif (bizz % 5) == 0: #elif is bizz equal to a multiple of 5?
        print ("Fizz")
        bizz = bizz + 1 #iterate + 1 to bizz, elif statement terminates
    else (bizz % 5) == 0 and (bizz % 3) == 0:
        print ("Fizzbuzz")
        bizz = bizz +1 #iterate + 1 to bizz, if statement terminates, loops begins
#exception handling, make sure any other 
    #else:
      #  print (bizz)
        #bizz = bizz +1

