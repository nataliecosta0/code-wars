"""
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""

def solution(s):
    pair = ''
    two_letters = []
    for x in s:
        pair = pair + x
        if len(pair) == 2:
            two_letters.append(pair)
            pair = ''
    if pair:
        two_letters.append(pair + '_')
    return two_letters

print(solution("asdfads"))