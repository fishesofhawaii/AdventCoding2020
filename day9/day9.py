with open('input.txt', 'r') as read_obj:
    preamble_size = 25
    data_list = []
    for row in read_obj:
        clean_row = row.strip()
        data_list.append(int(clean_row))

    index = preamble_size
    while index < len(data_list):
        data_point = data_list[index]

        previous_preamble_list = data_list[index-preamble_size:index]
        did_find = False
        # Iterate 
        for preamble_item in previous_preamble_list:
            if data_list[index] - preamble_item in previous_preamble_list and data_list[index] / 2 != preamble_item:
                did_find = True

        if not did_find:
            print("Didnt find one!", data_list[index])
            break

        index += 1
