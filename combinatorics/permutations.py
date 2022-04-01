def permutations_prefix_processing(A):
    result = []
    N = len(A)
    def permute(index):
        if index == N:
            result.append(A[:])
            return 
        
        for i in range(index, N):
            A[index] , A[i] = A[i] , A[index]
            permute(index + 1)
            A[index] , A[i] = A[i] , A[index]
    
    permute(0)
                                                    
    return result