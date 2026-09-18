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

def get_sensor_reading(grid, position):

    row, col = position

    sensors = {}

    # Up
    if row == 0 or grid[row - 1][col] == "X":
        sensors["up"] = True
    else:
        sensors["up"] = False

    # Down
    if row == len(grid) - 1 or grid[row + 1][col] == "X":
        sensors["down"] = True
    else:
        sensors["down"] = False

    # Left
    if col == 0 or grid[row][col - 1] == "X":
        sensors["left"] = True
    else:
        sensors["left"] = False

    # Right
    if col == len(grid[0]) - 1 or grid[row][col + 1] == "X":
        sensors["right"] = True
    else:
        sensors["right"] = False

    return sensors

def get_possible_locations(grid):

    possible_locations = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):

            if grid[row][col] != "X":
                possible_locations.append((row, col))

    return possible_locations

def filter_locations(grid, possible_locations, sensor_reading):

    matching_locations = []

    for location in possible_locations:

        location_sensor = get_sensor_reading(grid, location)

        if location_sensor == sensor_reading:
            matching_locations.append(location)

    return matching_locations

def move_possible_locations(grid, possible_locations, direction):

    new_locations = []

    for location in possible_locations:

        possible_moves = get_possible_moves(grid, location)

        if direction in possible_moves:

            new_position = move_robot(location, direction)

            new_locations.append(new_position)

    return new_locations

def update_locations(grid, possible_locations, sensor_reading):

    updated_locations = []

    for location in possible_locations:

        location_sensor = get_sensor_reading(grid, location)

        if location_sensor == sensor_reading:
            updated_locations.append(location)

    return updated_locations

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

sensor_reading = get_sensor_reading(grid, new_position)

print("\nSensor Reading:")

print("Wall Up:", sensor_reading["up"])
print("Wall Down:", sensor_reading["down"])
print("Wall Left:", sensor_reading["left"])
print("Wall Right:", sensor_reading["right"])

possible_locations = get_possible_locations(grid)

print("\nPossible Robot Locations:")

for location in possible_locations:
    print(location)

matching_locations = filter_locations(
    grid,
    possible_locations,
    sensor_reading
)

print("\nLocations Matching Sensor Reading:")

for location in matching_locations:
    print(location)

updated_locations = move_possible_locations(
    grid,
    matching_locations,
    "right"
)

print("\nPossible Locations After Moving Right:")

for location in updated_locations:
    print(location)


localized_locations = update_locations(
    grid,
    updated_locations,
    sensor_reading
)

print("\nLocations After New Sensor Reading:")

for location in updated_locations:
    print(location)