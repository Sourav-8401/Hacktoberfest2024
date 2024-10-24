def lcs(X, Y):
    # Get the lengths of the two sequences
    m = len(X)
    n = len(Y)
    
    # Create a 2D table to store lengths of longest common subsequence
    # Initialize with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # When characters match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The length of the longest common subsequence is dp[m][n]
    
    # To find the LCS string, let's backtrack from dp[m][n]
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        # If current characters in both strings are the same, it's part of the LCS
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        # If not, find the larger value in the previous row or column
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    # Since we traversed the LCS backwards, reverse the string
    lcs_str.reverse()
    
    return ''.join(lcs_str), dp[m][n]

# Example usage
X = "ABCBDAB"
Y = "BDCAB"
lcs_str, length = lcs(X, Y)
print(f"Longest Common Subsequence: {lcs_str}, Length: {length}")
