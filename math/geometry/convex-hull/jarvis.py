class Solution:
    def orientation(self, p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) 
    def between(self, p, i, q):
        a = (i[0] >= p[0] and i[0] <= q[0]) or (i[0] <= p[0] and i[0] >= q[0])
        b = (i[1] >= p[1] and i[1] <= q[1]) or (i[1] <= p[1] and i[1] >= q[1])
        return a and b
        
    def outerTrees(self, t):
        T = len(t)
        if T < 4: return t                
        hull = set()        
        leftiest = 0        
        for i in range(1, T):
            if t[leftiest] > t[i]: leftiest = i
                
        curr = leftiest
                
        while True:
            q = (curr + 1) % T            
            for i in range(T):
                if i not in [q, curr] and self.orientation(t[curr], t[i], t[q]) < 0:
                    q = i                        
            hull.add(tuple(t[q]))
            curr = q            
            if curr == leftiest: break                                
        return hull
                
            
        
        