import math
from collections.abc import Iterable
from binary_int_transformations import *


def elias_code (number):
    
    if isinstance(number, Iterable) and not isinstance(number, str):
        return ''.join([elias_code(num) for num in number])
    
    integer = number if isinstance(number, int) else binary_to_int(number)
    result = '0'
    
    while (True):
        log = int(math.log(integer, 2))
        if log==0:
            break
        result = int_to_binary(integer) + result
        integer = log
        
    return result


def elias_decode (numbers):
    
    binaries = []
    
    length = 0
    
    while (numbers):
        look = numbers[:length+1]
        numbers = numbers[length+1:]
        if look[-1] == '0':
            binaries.append('1'+look[:-1])
            length = 0
        else:
            length = binary_to_int('1'+look[:-1])
                
    return [binary_to_int(binary) for binary in binaries]