def largest_rect_area_stack(self, H):
    max_rect = 0
    N = len(H)
    stack = [-1]
    
    for i, h in enumerate(H):
        while stack[-1] != -1 and h <= H[stack[-1]]:
            max_rect = max(max_rect, H[stack.pop()] * (i - 1 - stack[-1]))
        stack.append(i)
        
    while stack[-1] != -1:
        max_rect = max(max_rect, H[stack.pop()] * (N - stack[-1] - 1))
    
    return max_rect

def largest_rect_area_Div_and_Con(self, H):
    def area(L, R):
        if  L > R: return 0
        if  L == R: return H[L]
        
        min_index = L
        
        for i in range(L, R + 1):
            if H[i] < H[min_index]:
                min_index = i
        
        return max(H[min_index]*(R-L+1), area(L, min_index - 1), area(min_index + 1, R))
                    
    return area(0, len(H) - 1)     