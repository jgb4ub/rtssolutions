#Using Python 3.9.1

'''
param1: integer input value for comparison
param2: integer list

Compares param1 to each value in integer list. Prints number of values above and below param1 in list.
'''
def rotate(string, rotation):
    if not rotation:
        print(string)
        return None
    print(string[-rotation:] + string[0:-rotation])

#####   tests   #####

rotate('Farmers', 0)

rotate('Farmers', 3)

rotate('Farmers', -3)