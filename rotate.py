#Using Python 3.9.1

'''
param1: String to rotate
param2: Integer value by which to rotate

Rotates param1 by the value input as param2.
'''
def rotate(string, rotation):
    if not rotation:
        print(string)
        return None
    print(string[-rotation:] + string[0:-rotation])

#####   tests   #####

# rotate('Farmers', 0)

# rotate('Farmers', 3)

# rotate('Farmers', -3)

# rotate('s', 0)

# rotate('s', 3)

# rotate('sdfg', -3)

# rotate('', 0)

# rotate('', 3)

# rotate('', -3)