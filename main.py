grid = [
    [".", ".", ".", ".", "."],
    [".", "X", ".", ".", "."],
    [".", ".", "R", ".", "."],
    [".", ".", ".", "X", "."],
    [".", ".", ".", ".", "G"]
]


def find_position(grid, symbol):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == symbol:
                return (row, col)


print("Robot Environment:\n")

for row in grid:
    for cell in row:
        print(cell, end=" ")
    print()

robot_position = find_position(grid, "R")
goal_position = find_position(grid, "G")

print("\nRobot Position:", robot_position)
print("Goal Position:", goal_position)