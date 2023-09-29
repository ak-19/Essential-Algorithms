class FenwickTreeCounter:
    """
    Fenwick Tree (Binary Indexed Tree) 
    used as counter 
    input: int max value allowed, must be small enough to fit in memory a array length of max_val + 1    
    """
    def __init__(self, max_val):
        self.bit = [0] * (max_val + 1)
        self.N = max_val
                        
    def update(self, val):
        while val <= self.N:
            self.bit[val] += 1
            val += val & -val
    
    def get_count_upto(self, val):
        count = 0
        while val > 0:
            count += self.bit[val]               
            val -= val & -val            
        return count