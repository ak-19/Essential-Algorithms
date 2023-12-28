def forbenius(p1, p2):
    """Returns the maximum value that can be obtained with coin 2 denominations"""
    #https://en.wikipedia.org/wiki/Coin_problem
    return p1 * p2 - p1 - p2 