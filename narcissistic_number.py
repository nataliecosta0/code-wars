"""
A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. 
In this Kata, we will restrict ourselves to decimal (base 10).
"""

def narcissistic( value ):
    result = 0
    output = [int(d) for d in str(value)]
    count = len(output)
    for x in output:
        result = result + (x ** count)
        
    if result == value:
        return True
    else:
        return False