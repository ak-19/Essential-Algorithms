class RabinKarp:
    def __init__(self, pattern) -> None:
        self.p = pattern
        self.P = len(pattern)
        self.hash = 0
        self.mod = 1_000_000_007 
        self.base = 31
        self.rm = 1 # max power, used to remove left most char efficiently
        for i in range(len(pattern) - 1):
            self.rm = (self.rm * self.base) % self.mod
        for i in range(len(pattern)):
            self.hash = (self.hash * self.base + ord(pattern[i]) - ord('a') + 1) % self.mod

    def find_matches(self, text):
        matches = []
        T = len(text)
        h = 0
        for i in range(self.P):
            h = ((h * self.base) % self.mod + (ord(text[i]) - ord('a') + 1)) % self.mod

        if h == self.hash:
            matches.append(0)
        
        for i in range(self.P, T):
            h -= ((ord(text[i - self.P]) - ord('a') + 1) * self.rm) % self.mod            
            h = ((h * self.base) % self.mod + (ord(text[i]) - ord('a') + 1)) % self.mod 
            if h == self.hash: matches.append(i - self.P + 1)

        return matches       