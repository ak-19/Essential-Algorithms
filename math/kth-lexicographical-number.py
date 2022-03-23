class KthLexicographicalNumber:
    def count_subnodes(self, node, next_node, n):        
        count = 0        
        while node <= n:
            count += min(n + 1, next_node)  - node            
            node *= 10
            next_node *= 10        
        return count
    
    def findKthNumber(self, n: int, k: int) -> int:  
        curr = 1
        k -= 1
        while k:
            count = self.count_subnodes(curr, curr + 1, n)
            
            if count <= k:
                k -= count
                curr += 1
            else:
                k -= 1
                curr *= 10
                        
        return curr

print(KthLexicographicalNumber().findKthNumber(20,3))