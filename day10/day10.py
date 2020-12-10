with open('input.txt', 'r') as read_obj:
    adapter_joltage_list = [0]
    for row in read_obj:
        clean_row = row.strip()
        adapter_joltage_list.append(int(clean_row))
    
    adapter_joltage_list.sort()
    adapter_joltage_list.append(adapter_joltage_list[-1] + 3)

    index = 0
    diff_1 = 0
    diff_3 = 0
    while index < len(adapter_joltage_list) - 1:
        diff = adapter_joltage_list[index + 1] - adapter_joltage_list[index]

        if diff == 1:
            print("Adding to 1 list{", adapter_joltage_list[index], adapter_joltage_list[index + 1], "}")
            diff_1 += 1
        elif diff == 3:
            print("Adding to 3 list{", adapter_joltage_list[index], adapter_joltage_list[index + 1], "}")
            diff_3 += 1

        index += 1

    print(diff_1 * diff_3)