# Junmao Lin
# while loop

gravity = -9.8 # downward acceleration due to gravity is -9.8 meters per second^2
# v is the initial horizontal velocity of the ball in meters per second
# h is the initial height of the ball in meters
def how_far(v, h):
    t = -1.0 # seconds traveled
    d = h # distance to ground
    while d >= 0:
        t += 1
        d = h + (0.5)*(gravity * (t*t))
        
    distance_traveled = v * t
    return distance_traveled


if __name__ == "__main__":
    test1 = how_far(10.0, 100.0)
    print("how_far(10.0, 100.0) is:", test1)
    print()
    test2 = how_far(45.0, 2.0)
    print("how_far(45.0, 2.0) is:", test2)
    print()
    test3 = how_far(20.0, 100.0)
    print("how_far(20.0, 100.0) is:", test3)
    print()
    test4 = how_far(30.0, 100.0)
    print("how_far(30.0, 100.0) is:", test4)
    print()
    test5 = how_far(20.0, 10000.0)
    print("how_far(20.0, 10000.0) is:", test5)
    print()
