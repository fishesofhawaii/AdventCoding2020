def find_encryption_weakness(number, data_list): 
    index = 0
    while index < len(data_list):
        rolling_list = []
        current_index = index

        while current_index < len(data_list):
            rolling_list.append(data_list[current_index])
            if sum(rolling_list) == number:
                return min(rolling_list) + max(rolling_list)
            elif sum(rolling_list) > number:
                break # break the inside loop
            current_index += 1

        index += 1

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

    response = find_encryption_weakness(data_list[index], data_list)
    print("Final answer", response)