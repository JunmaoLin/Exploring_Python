# Junmao Lin
# If, else


def tip_amount(bill, good_service):
    if (bill is None or good_service is None):
        return -1
    if (bill < 0): # bill should not be less than 0.
        return -1

    if (bill <= 30.00):
        return 8.00
    else: #(bill > 30.00)
        if (good_service):
            return bill * 0.29
        else: #(not good_service)
            return bill * 0.16


if __name__ == "__main__":
    print("tip_amount(23.37,True) is", tip_amount(23.37, True))
    print()
    print("tip_amount(23.37,False) is", tip_amount(23.37, False))
    print()
    print("tip_amount(81.75,True) is", tip_amount(81.75, True))
    print()
    print("tip_amount(63.59,True) is", tip_amount(63.59, True))
    print()
    print("tip_amount(63.59,False) is", tip_amount(63.59, False))
    print()
