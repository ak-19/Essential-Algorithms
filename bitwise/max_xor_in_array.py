def find_maximum_xor_with_hashing(nums):
    L = len(bin(max(nums))) - 2

    max_xor = 0

    for i in range(L)[::-1]:
        max_xor <<= 1
        curr = max_xor | 1
        prefixes = {num >> i for num in nums}
        max_xor |= any(curr ^ p in prefixes for p in prefixes)
                
    return max_xor

print(find_maximum_xor_with_hashing([3,10,5,25,2,8]) == 28)
print(find_maximum_xor_with_hashing([14,70,53,83,49,91,36,80,92,51,66,70]) == 127)

def findMaximumXOR(nums):
    L = len(bin(max(nums))) - 2
    max_xor = 0
    
    nums = [[(num >> i) & 1  for i in range(L)[::-1]] for num in nums]
    
    trie = dict()
    
    for num in nums:
        
        node = xor_node = trie
        accumulated_val = 0
        
        for bit in num:
            if bit not in node:
                node[bit] = dict()
                
            node = node[bit]
            
            rev_bit = (bit + 1) % 2
            # rev_bit = 1 - bit # alternative
            
            accumulated_val <<= 1
            if rev_bit in xor_node:
                accumulated_val |= 1
                xor_node = xor_node[rev_bit]
            else:
                xor_node = xor_node[bit]            
        
        max_xor = max(max_xor, accumulated_val)
    
    return max_xor


print(findMaximumXOR([3,10,5,25,2,8]) == 28)
print(findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]) == 127)