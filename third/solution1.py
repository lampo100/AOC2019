from typing import List, Dict, Tuple
Grid = Dict[int, Dict[int, bool]]
Point = Tuple[int, int]

def map_cable(origin_point: Point, movement_table: List[str]) -> Grid:
    current_point = origin_point
    position_table = dict()
    for move in movement_table:
        direction = move[0]
        steps = int(move[1:])
        if direction == 'L':
            move_left(current_point, steps, position_table)
            current_point = (current_point[0], current_point[1] - steps)
        elif direction == 'R':
            move_right(current_point, steps, position_table)
            current_point = (current_point[0], current_point[1] + steps)
        elif direction == 'U':
            move_up(current_point, steps, position_table)
            current_point = (current_point[0] + steps, current_point[1])
        elif direction == 'D':
            move_down(current_point, steps, position_table)
            current_point = (current_point[0] - steps, current_point[1])
        else:
            raise Exception("Wrong direction code")
    return position_table

def move_left(current_point: Point, steps: int, position_table: Grid):
    row = current_point[0]
    column = current_point[1]
    position_table.setdefault(row, {column - steps : True})[column - steps] = True

def move_right(current_point: Point, steps: int, position_table: Grid):
    row = current_point[0]
    column = current_point[1]
    position_table.setdefault(row, {column + steps : True})[column + steps] = True

def move_up(current_point: Point, steps: int, position_table: Grid):
    row = current_point[0]
    column = current_point[1]
    position_table.setdefault(row + steps, {column : True})[column] = True

def move_down(current_point: Point, steps: int, position_table: Grid):
    row = current_point[0]
    column = current_point[1]
    position_table.setdefault(row - steps, {column : True})[column] = True

def smallest_distance(origin_point: Point, first_grid: Grid, second_grid: Grid) -> int:
    intersections = []
    for row in first_grid.keys():
        for column in first_grid[row].keys():
            if second_grid.get(row):
                if second_grid[row].get(column):
                    intersections.append((row, column))

    return min([manhattan_distance(x, origin_point) for x in intersections])

def manhattan_distance(x: Point, y: Point) -> int:
    return abs(x[0] - y[0]) + abs(x[1] - y[1])



if __name__ == '__main__':
    with open('./input') as file:
        first_cable_movement_table = [x for x in file.readline().split(',')]
        second_cable_movement_table = [x for x in file.readline().split(',')]
    first_grid = map_cable((0, 0), first_cable_movement_table)
    second_grid = map_cable((0, 0), second_cable_movement_table)
    print(smallest_distance((0, 0), first_grid, second_grid))
