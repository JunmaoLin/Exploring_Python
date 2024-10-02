# Junmao Lin
# If statements

def population(year):
    # a positive integer called year that is greater than or equal to 2000,
    # representing a four-digit year.
    if (year >= 2000 and year <= 9999):
         return ((((year%100) - 10) * 3) + 310)
    return -1

if __name__ == "__main__":
    test1 = population(2001)
    print("population(2001) is", test1)
    print()
    test2 = population(2010)
    print("population(2010) is", test2)
    print()
    test3 = population(2016)
    print("population(2016) is", test3)
    print()

