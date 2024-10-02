# Junmao Lin
# casting

def how_long(distance, fraction, scale): #distance is in miles
    c = 186000 # This is in miles/second
    if(distance < 0): # distance should never be less than 0, since it is a scalar quantity
        return -1

    #convert everything to float to prevent rounding errors
    timeInSeconds = float(distance)/(float(c)*float(fraction)) 
    
    if (scale == 'Y'):
        return timeInSeconds/float(60*60*24*365) #sec to min to hour to day to year
    elif (scale == 'D'):
        return timeInSeconds/float(60*60*24) #sec to min to hour to day
    elif (scale == 'H'):
        return timeInSeconds/float(60*60) #sec to min to hour
    elif (scale == 'M'):
        return timeInSeconds/float(60) #sec to min
    else:
        return -1 # Otherwise

if __name__ == "__main__":
    test1 = how_long(238900, 0.01, "M") # approximate distance to Moon
    print("how_long(238900, 0.01, 'M') is:", test1)
    print()
    test2 = how_long(45594000, 0.01, "H") # approximate distance to Mars
    print("how_long(45594000, , 0.01, 'H') is:", test2)
    print()
    test3 = how_long(93000000, 1.0, "M") # approximate distance to Sun
    print("how_long(93000000, 1.0, 'M') is:", test3)
    print()
    test4 = how_long(9000000000, 0.01, "D") # approximate distance to edge of Solar System
    print("how_long(9000000000, 0.01, 'D') is:", test4)
    print()
    test5 = how_long(25000000000000, 0.01, "Y") # approximate distance to closest system Alpha Centauri
    print("how_long(25000000000000, 0.01, 'Y') is:", test5)
    print()

