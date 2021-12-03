class Solution:         
    def find(self, start, end, cuts, s):
        L, R = start, end
        while L >= 0 and R < len(s) and s[L] == s[R]:
            curr_cut = None
            if L == 0:
                curr_cut = 0
            else:
                curr_cut = cuts[L - 1] + 1
                
            cuts[R] = min(cuts[R], curr_cut)
            L -= 1
            R += 1
 
    def minCut(self, s: str) -> int:
        N = len(s)
        cuts = [i for i in range(N)]        
        for mid in range(N):
            self.find(mid, mid, cuts,s)
            self.find(mid - 1, mid, cuts,s)                    
        return cuts[N - 1]