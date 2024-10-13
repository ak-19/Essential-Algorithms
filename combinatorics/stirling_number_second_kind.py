# """
# Stirling number of a second kind
# """

from functools import cache


class StirlingNumberSecondKind:
    def stirling_numbers_second_kind_bottomup_table(self, n):
        """
        This function generates the bottom-up DP table for Stirling numbers of the second kind S(n,k).        
        The DP table is a 2D array dp where dp[i][j] = S(i,j) is the number of ways to partition a set of i items into j nonempty subsets.        
        The function returns the DP table dp, which is a 2D list of size (n + 1) x (n + 1).
        Faster then recursive.        
        Parameters
        ----------
        n : int
            The number of items in the set.
        
        Returns
        -------
        list
            The bottom-up DP table.
        """    
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        # Base cases
        for i in range(1, n + 1):
            dp[i][1] = 1
            dp[i][i] = 1
        
        # Fill the DP table
        for i in range(2, n + 1):
            for j in range(2, i):
                dp[i][j] = j * dp[i - 1][j] + dp[i - 1][j - 1]
        
        return dp    

    @cache
    def stirling_number_second_kind(self, n, k):
        """
        Calculate Stirling numbers of the second kind.
        
        The Stirling number of the second kind, denoted as S(n,k), counts the number of ways to partition a set of n items into k nonempty subsets.
        
        Parameters
        ----------
        n : int
            The number of items in the set.
        k : int
            The number of subsets to partition into.
        
        Returns
        -------
        int
            The number of ways to partition a set of n items into k nonempty subsets.
        """
        if k == 1 or k == n:
            return 1
        if k == 0 or k > n:
            return 0
        return k * self.stirling_number_second_kind(n - 1, k) + self.stirling_number_second_kind(n - 1, k - 1)

    def print_stirling_table(self, n):
        """
        Print the Stirling numbers of the second kind in a table up to n.

        The first column is the number of items in the set, and the second column is the number of subsets to partition into.
        The entries in the table represent the number of ways to partition a set of n items into k nonempty subsets.

        Parameters
        ----------
        n : int
            The number of rows in the table.
        """
        for i in range(1, n + 1):
            row = [self.stirling_number_second_kind(i, j) for j in range(1, i + 1)]
            print(f"n={i}: {row}")
