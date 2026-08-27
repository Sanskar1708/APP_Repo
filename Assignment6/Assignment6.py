def knapsack_bottom_up(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


def knapsack_top_down(values, weights, W, n, memo=None):
    if memo is None:
        memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    if n == 0 or W == 0:
        return 0

    if memo[n][W] != -1:
        return memo[n][W]

    if weights[n - 1] > W:
        memo[n][W] = knapsack_top_down(values, weights, W, n - 1, memo)
        return memo[n][W]

    include_item = values[n - 1] + knapsack_top_down(values, weights, W - weights[n - 1], n - 1, memo)
    exclude_item = knapsack_top_down(values, weights, W, n - 1, memo)

    memo[n][W] = max(include_item, exclude_item)

    return memo[n][W]


if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    n = len(values)

    print(f"Bottom-Up Max Profit: {knapsack_bottom_up(values, weights, W)}")
    print(f"Top-Down Max Profit: {knapsack_top_down(values, weights, W, n)}")
