def traverseDownward(terrain_list, right_movement, down_movement):
    current_x = 0
    current_y = 0

    tree_hits = 0

    while current_y < len(terrain_list) - 1:
        row = terrain_list[current_y]

        current_x = (current_x + right_movement) % (len(row) - 1)
        current_y = current_y + down_movement
        
        landing_spot = terrain_list[current_y][current_x]

        if landing_spot == "#": 
            tree_hits = tree_hits + 1
        elif landing_spot == ".":
            a = 1
        else: 
            print("Unexpected!")

    print("Got", tree_hits," tree hits on this slope")
    return tree_hits


with open('input.txt', 'r') as read_obj:
    terrain_list = []

    for row in read_obj:
        terrain_list.append(row)

    slope1 = traverseDownward(terrain_list, 1, 1)
    slope2 = traverseDownward(terrain_list, 3, 1)
    slope3 = traverseDownward(terrain_list, 5, 1)
    slope4 = traverseDownward(terrain_list, 7, 1)
    slope5 = traverseDownward(terrain_list, 1, 2)

    slope_product = slope1 * slope2 * slope3 * slope4 * slope5
    print("The product of all the slope tree hits is:", slope_product)

