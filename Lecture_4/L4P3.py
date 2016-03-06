def stdDevOfLengths(L):
    """L: a list of strings
    returns: float, the standard deviation of the lengths of the strings,
    or NaN if L is empty."""
    if len(L) == 0:
        return float('NaN')
    else:
        sum = 0
        for ele in L:
            sum += len(ele)
        mean = sum/float(len(L))
        summation = 0
        for ele in L:
            summation += (len(ele) - mean)**2 /len(L)
        return summation ** 0.5

L = ['a', 'z', 'p']
print stdDevOfLengths(L)