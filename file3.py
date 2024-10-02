# Junmao Lin
# arithmetics

def getSeconds(days, hours, minutes):
    intdays = int(days)
    inthours = int(hours)
    intmins = int(minutes)

    seconds = ((((intdays * 24) + inthours) * 60) + intmins) * 60
    return seconds

if __name__ == "__main__":
    time1 = "11:11:14"
    d1, h1, m1 = time1.split(":")
    print('getSeconds("' + time1 + '") is', getSeconds(d1, h1, m1))
    print()
    time2 = "00:01:02"
    d2, h2, m2 = time2.split(":")
    print('getSeconds("' + time2 + '") is', getSeconds(d2, h2, m2))
    print()
    time3 = "05:00:30"
    d3, h3, m3 = time3.split(":")
    print('getSeconds("' + time3 + '") is', getSeconds(d3, h3, m3))
    print()
    time4 = "00:00:00"
    d4, h4, m4 = time4.split(":")
    print('getSeconds("' + time4 + '") is', getSeconds(d4, h4, m4))
    print()
    time5 = "02:18:49"
    d5, h5, m5 = time5.split(":")
    print('getSeconds("' + time5 + '") is', getSeconds(d5, h5, m5))
    print()
