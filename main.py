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

def get_possible_moves(grid, position):

    row, col = position

    moves = []

    # Up
    if row > 0 and grid[row - 1][col] != "X":
        moves.append("up")

    # Down
    if row < len(grid) - 1 and grid[row + 1][col] != "X":
        moves.append("down")

    # Left
    if col > 0 and grid[row][col - 1] != "X":
        moves.append("left")

    # Right
    if col < len(grid[0]) - 1 and grid[row][col + 1] != "X":
        moves.append("right")

    return moves

def move_robot(position, direction):

    row, col = position

    if direction == "up":
        return (row - 1, col)

    elif direction == "down":
        return (row + 1, col)

    elif direction == "left":
        return (row, col - 1)

    elif direction == "right":
        return (row, col + 1)

print("Robot Environment:\n")

for row in grid:
    for cell in row:
        print(cell, end=" ")
    print()

robot_position = find_position(grid, "R")
goal_position = find_position(grid, "G")

print("\nRobot Position:", robot_position)
print("Goal Position:", goal_position)

possible_moves = get_possible_moves(grid, robot_position)

print("Possible Moves:", possible_moves)

if "right" in possible_moves:

    new_position = move_robot(robot_position, "right")

    print("\nRobot moved: right")
    print("New Position:", new_position)