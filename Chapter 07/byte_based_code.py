from collections.abc import Iterable
from binary_int_transformations import *

def byte_based_code (number, byte_length):
    
    if isinstance(number, Iterable) and not isinstance(number, str):
        return ''.join([byte_based_code(num, byte_length) for num in number])
    
    integer = number if isinstance(number, int) else binary_to_int(number)
    
    base = 2**(byte_length-1)
    
    result = '1' * byte_length
    while(True):
        rest = integer % base
        integer = integer // base
        add = int_to_binary(rest)
        result = '0'*(byte_length - len(add)) + add + result
        if integer==0:
            return result
        
        
def byte_based_decode (numbers, byte_length):
    
    binaries = []
    
    numbers = '0' * (len(numbers) % byte_length) + numbers
    
    base = 2**(byte_length-1)
    
    number = 0
    while (numbers):
        look = numbers[:byte_length]
        numbers = numbers[byte_length:]
        if look == '1'*byte_length:
            binaries.append(number)
            number = 0
        else:
            number = number * base + binary_to_int(look)
                
    return binaries