def execute_program(operations, quantities, accumulator, row_list, index):
    acc = accumulator
    r_list = row_list.copy()
    i = index
    
    while i not in r_list:
        if i > len(operations) - 1:
            break

        r_list.append(i)

        op = operations[i]
        num = get_num(quantities[i])

        if op == "acc":
            acc += num
            i += 1
        elif op == "jmp":
            i += num
        elif op == "nop":
            i += 1
        else:
            print("Dont know how to handle this", op)

    if len(operations) == i:
        print("Finished execution at", i, "accumulator:", acc)

def get_num(raw_num):
    return int(raw_num)

def get_modified_operations(operations, row, new_op):
    copy_list = operations.copy()
    copy_list[row] = new_op

    return copy_list

with open('input.txt', 'r') as read_obj:
    operations = []
    quantities = []
    for row in read_obj:
        clean_row = row.strip()
        operation_quantity_list = clean_row.split(" ")
        
        operations.append(operation_quantity_list[0])
        quantities.append(operation_quantity_list[1])

    
    index = 0
    accumulator = 0
    row_list = []
    print("THERE ARE A TOTAL OF", len(operations), "OPERATIONS")
    # LETS BRUTE FORCE IT
    while index not in row_list:
        if index > len(operations):
            break

        row_list.append(index)

        op = operations[index]
        num = get_num(quantities[index])

        if op == "acc":
            accumulator += num
            index += 1
        elif op == "jmp":
            execute_program(get_modified_operations(operations, index, "nop"), quantities, 0, [], 0)
            index += num
        elif op == "nop":
            execute_program(get_modified_operations(operations, index, "jmp"), quantities, 0, [], 0)
            index += 1
        else:
            print("Dont know how to handle this", op)
