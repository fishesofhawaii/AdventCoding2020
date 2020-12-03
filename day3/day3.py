def traverseDownward(terrain_list, right_movement, down_movement):
    current_x = 0
    current_y = 0

    tree_hits = 0

    while current_y < len(terrain_list):
        row = terrain_list[current_y]

        landing_spot = terrain_list[current_y][current_x % (len(row) - 1)]
        if landing_spot == "#": 
            tree_hits = tree_hits + 1

        current_x = current_x + right_movement
        current_y = current_y + down_movement
    print("You hit", tree_hits, "trees!")








with open('input.txt', 'r') as read_obj:
    terrain_list = []

    for row in read_obj:
        terrain_list.append(row)

    traverseDownward(terrain_list, 3, 1)



