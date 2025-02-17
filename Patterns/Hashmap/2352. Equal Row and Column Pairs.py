from collections import defaultdict
def equalPairs(grid):
    r = defaultdict(int)
    res = 0
    for i in range(len(grid)):
        r[tuple(grid[i])] += 1
    for column in zip(*grid):
        res += r[column]
    return res
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(equalPairs(grid))