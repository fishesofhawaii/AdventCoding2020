def get_response(mask, binary_string):
    index = 0
    response_string = ""

    while index < len(mask):
        if mask[index] == binary_string[index]:
            response_string += mask[index]
        elif mask[index] == "1":
            response_string += "1"
        elif mask[index] == "X":
            response_string += "X"
        else: 
            response_string += binary_string[index]
        
        index += 1


    response_list = [response_string]
    x_index = response_string.find("X")

    while x_index != -1:
        temp_list = []
        for response in response_list:
            l_0 = list(response)
            l_1 = list(response)

            l_0[x_index] = "0"
            l_1[x_index] = "1"

            temp_list += ["".join(l_0), "".join(l_1)]
        
        response_list = temp_list.copy()
        x_index = response_list[0].find("X")

    return response_list
        
def get_mem_slot(s):
    # Comes in as "mem[####]" we just want ####
    return s.split("[")[1].split("]")[0]

def get_binary_value(data):
    return '0b{:036b}'.format(int(data))

def get_mask_value(data):
    return "0b" + data

with open('input.txt', 'r') as read_obj:
    member_berries = {}
    mask = "x" 
    for row in read_obj:
        clean_row = row.strip()
        split_row = clean_row.split("=")
        
        left_side = split_row[0].strip()
        right_side = split_row[1].strip()

        if left_side == "mask":
            mask = get_mask_value(right_side)
        else:
            slot = get_mem_slot(left_side)
            binary_slot = get_binary_value(get_mem_slot(left_side))
            # # Need to decode for part 2
            slot_list = get_response(mask, binary_slot)

            for slot in slot_list:
                member_berries[eval(slot)] = int(right_side)

    total = 0
    for k, v in member_berries.items():
        total += v

    print(total)