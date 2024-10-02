# Junmao Lin
# if else with arithmetics

def temp_converter(temperature, new_unit):
    if(new_unit == 'C'):
        return ((temperature-32)*5)/9
    elif (new_unit == 'F'):
        return ((temperature*9)/5)+32
    else:
        return None #invalid new_unit

if __name__ == "__main__":
    print("temp_converter(100,'C') is", temp_converter(100, 'C'))
    print()
    print("temp_converter(0,'F') is", temp_converter(0, 'F'))
    print()
    print("temp_converter(212,'C') is", temp_converter(212, 'C'))
    print()
    print("temp_converter(32,'C') is", temp_converter(32, 'C'))
    print()
    print("temp_converter(50,'F') is", temp_converter(50, 'F'))
    print()
