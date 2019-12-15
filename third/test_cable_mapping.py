from solution1 import map_cable, smallest_distance

def test_mapping():
    with open('./third/test_input1') as file:
        movement_table = file.readline().split(',')
    grid = map_cable((0, 0), movement_table)

    assert grid[0] == {8: True}
    assert grid[5] == {3: True, 8: True}
    assert grid[2] == {3: True}

def test_mapping_second():
    with open('./third/test_input2') as file:
        movement_table = file.readline().split(',')
    grid = map_cable((0, 0), movement_table)

    assert grid[7] == {0: True, 6: True}
    assert grid[3] == {2: True, 6: True}

def test_smallest_distance():
    with open('./third/test_input1') as file:
        movement_table = file.readline().split(',')
    grid1 = map_cable((0, 0), movement_table)
    with open('./third/test_input2') as file:
        movement_table = file.readline().split(',')
    grid2 = map_cable((0, 0), movement_table)
    smallest_distance((0, 0), grid1, grid2)