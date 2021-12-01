class CombinationsRecursive:
    def __init__(self, characters, combinationLength):
        self.combinations = []
        chars = list(sorted(list(characters)))
        N = len(chars)
        def generate(index = 0, curr = []):    
            if len(curr) == combinationLength:
                self.combinations.append(''.join(curr))
                return
            for i in range(index, N): generate(i + 1, curr + [chars[i]])
        generate()

    def get_combinations(self):
        return self.combinations

class CombinationsBitmasked:
    def __init__(self, characters, combinationLength):
        self.combinations = []
        N = len(characters)
        for bitmask in range(2**N, 0, -1):
            if bin(bitmask).count('1') == combinationLength:
                curr = [characters[j] for j in range(N) if bitmask & (1 << N - j - 1)]
                self.combinations.append(''.join(curr))            
    def get_combinations(self):
        return self.combinations        

class CombinationsKnuth:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n, k = len(characters), combinationLength
        
        # init the first combination
        nums = list(range(k)) + [n]
        
        j = 0
        while j < k:
            # add current combination
            curr = [characters[n - 1 - nums[i]] for i in range(k - 1, -1, -1)]
            self.combinations.append(''.join(curr))
            
            # Generate next combination.
            # Find the first j such that nums[j] + 1 != nums[j + 1].
            # Increase nums[j] by one.
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j
                j += 1
            nums[j] += 1
        self.combinations .reverse()
    def get_combinations(self):
        return self.combinations              

c = CombinationsKnuth("gkosu",3)

print(c.get_combinations())


# 00001
# 00010
# 11100

