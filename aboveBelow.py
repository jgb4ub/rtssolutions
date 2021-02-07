#Using Python 3.9.1

'''
param1: integer input value for comparison
param2: integer list

Compares param1 to each value in integer list. Prints number of values above and below param1 in list.
'''
def above_below( input, list):
    below = 0
    above = 0
    for num in list:
        if num > input:
            above += 1
        else:
            below += 1
    print("above: "+str(above)+"\nbelow: "+str(below))


#####   tests    ######

#above_below(3,[1,1,1,1])
#above_below(3,[4,4,4,4])

#above_below(-1,[3,3,-4])

#above_below(3,[])