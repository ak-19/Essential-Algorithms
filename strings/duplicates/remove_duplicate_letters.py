from collections import Counter

#1 - iterative greedy
def remove_duplicate_letters_counting(self, s: str) -> str:        
    result = ''        
    while s:
        count = Counter(s)            
        pos = 0            
        for i in range(len(s)):
            if s[i] < s[pos]: pos = i                    
            count[s[i]] -= 1
            if count[s[i]] == 0: break
        
        result += s[pos]
        s = s[pos+1:].replace(s[pos],'')
    
    return result

#2 - stack based
def remove_duplicate_letters_stack(s):        
    result = []                
    seen = set()        
    last = {c: i for i, c in enumerate(s)}        
    for i, c in enumerate(s):            
        if c not in seen:                
            while result and c < result[-1] and i < last[result[-1]]:
                seen.discard(result.pop())                                
            result.append(c)
            seen.add(c)                        
    return ''.join(result)