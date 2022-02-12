#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      1531
#
# Created:     12.02.2022
# Copyright:   (c) 1531 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def fibonacci(n):
    seq = [0,1]
    for i in range(2,n+1):
        number = seq[-1] + seq[-2]

        seq.append(number)
    return seq

print(fibonacci(8))
