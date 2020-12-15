def get_response(mask, binary_string):
    index = 0
    response_string = ""
    while index < len(mask):
        if mask[index] == binary_string[index]:
            response_string += mask[index]
        elif mask[index] == "0":
            response_string += "0"
        elif mask[index] == "1":
            response_string += "1"
        else: 
            response_string += binary_string[index]
        
        index += 1

    return response_string
        
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
            value = get_binary_value(right_side)
            res = get_response(mask, value)
            member_berries[slot] = eval(res)

    total = 0
    for v in member_berries.values():
        total += v

    print(total)