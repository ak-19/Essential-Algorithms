def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0: return '0'
    
    result = []
    
    if numerator * denominator < 0:
        result.append('-')
    
    divided = abs(numerator)
    divisor = abs(denominator)
    
    result.append(str(divided // divisor))
    
    remainder = divided % divisor
    
    if remainder == 0: return ''.join(result)
    
    result.append('.')
    
    cache = dict()
    
    while remainder != 0:
        
        if remainder in cache:
            result.insert(cache[remainder], '(')
            result.append(')')
            break
            
        cache[remainder] = len(result)
        remainder *= 10
        result.append(str(remainder // divisor))
        remainder %= divisor
    
    return ''.join(result)



# print(fractionToDecimal(2, 1) == '2')
print(fractionToDecimal(1, 6) == "0.1(6)")
# print(fractionToDecimal(1, 90) == "0.0(1)")
# print(fractionToDecimal(1, 333))
# print(fractionToDecimal(1, 17))