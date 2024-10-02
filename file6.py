#for loop
def divisible(n):
    divisible_list = []
    for i in range (1,10): #excluding 10
        if n%i == 0:
            divisible_list.append(True)
        else:
            divisible_list.append(False)
    return divisible_list
    
if __name__ == "__main__":
    test1 = divisible(126)
    print("divisible(126) is:", test1)
    print()
    test2 = divisible(20)
    print("divisible(20) is:", test2)
    print()
    test3 = divisible(1024)
    print("divisible(1024) is:", test3)
    print()
    test4 = divisible(17)
    print("divisible(17) is:", test4)
    print()
    test5 = divisible(539)
    print("divisible(539) is:", test5)
    print()
