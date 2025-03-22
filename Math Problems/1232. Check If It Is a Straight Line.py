def checkStraightLine(coordinates):
    a = 0
    b = 1
    for i in range(len(coordinates) - 1):
        if coordinates[i][a] + 1 != coordinates[i + 1][a] or coordinates[i][b] + 1 != coordinates[i + 1][b] :
            return False
    return True
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(checkStraightLine(coordinates))