def longest_palindromic_substring_quadratic(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    start = 0
    max_len = 1

    def expand(left: int, right: int) -> None:
        nonlocal start, max_len
        while left >= 0 and right < n and s[left] == s[right]:
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                start = left
            left -= 1
            right += 1

    for center in range(n):
        # Odd length palindrome
        expand(center, center)
        # Even length palindrome
        expand(center, center + 1)

    return s[start:start + max_len]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return longest_palindromic_substring_quadratic(s)
