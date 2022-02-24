from collections import Counter

class DivideAndConquer:
    def valid(self, count, k):
        for i in range(26):
            c = chr(ord('a') + i)
            if 0 < count[c] < k:
                return False        
        return True
        
    def find(self, lo, hi, s, k):
        if hi - lo + 1 < k: return 0        
        count = Counter(s[lo:hi+1])                
        for i in range(lo, hi + 1):
            if count[s[i]] < k:
                return max(self.find(lo, i - 1, s, k), self.find(i + 1, hi, s, k))            
        return hi - lo + 1
                        
    def longest_char_k_repeats_substring(self, s, k):                                            
        return self.find(0, len(s) - 1, s, k)


class SlidingWindow:
    '''
    max substring, such that the frequency of each character is at least k.
    '''
    def max_unique(self, s):
        seen = set()
        unique_count = 0
        for c in s:
            if c not in seen:
                unique_count += 1
                seen.add(c)
        return unique_count
                                
    def longest_char_k_repeats_substring(self, s, k):                                            
        result = 0
        N = len(s)
        for unique_count in range(1, self.max_unique(s) + 1):
            count = Counter()
            start = end = index = unique = at_least_k = 0
            
            while end < N:
                if unique <= unique_count:
                    if count[s[end]] == 0: unique += 1
                    count[s[end]] += 1
                    if count[s[end]] == k: at_least_k += 1
                    end += 1
                else:
                    if count[s[start]] == k: at_least_k -= 1
                    count[s[start]] -= 1
                    if count[s[start]] == 0: unique -= 1
                    start += 1
                    
                if unique == unique_count and unique == at_least_k:
                    result = max(result, end - start)
            
        
        return result
                
