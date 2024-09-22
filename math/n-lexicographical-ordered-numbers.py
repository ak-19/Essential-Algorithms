from typing import List

def generateLexicographicalNumbers(n: int) -> List[int]:
    """
    Generates the first n lexicographical ordered numbers
    :param n: How many numbers to generate
    :return: A list of the first n lexicographical ordered numbers
    """
    A, curr = [], 1
    for _ in range(n):
        A.append(curr)
        if curr * 10 <= n: curr *= 10
        else:
            while curr % 10 == 9 or curr >= n: curr //= 10
            curr += 1        
    return A

print(generateLexicographicalNumbers(13))