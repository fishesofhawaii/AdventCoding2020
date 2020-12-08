def get_num(raw_num):
    return int(raw_num)

with open('input.txt', 'r') as read_obj:
    operations = []
    quantities = []
    for row in read_obj:
        clean_row = row.strip()
        operation_quantity_list = clean_row.split(" ")
        
        operations.append(operation_quantity_list[0])
        quantities.append(operation_quantity_list[1])

    print(operations)

    row_list = []
    index = 0
    accumulator = 0
    while index not in row_list:
        row_list.append(index)

        op = operations[index]
        num = get_num(quantities[index])

        if op == "acc":
            accumulator += num
            index += 1
        elif op == "jmp":
            index += num
        elif op == "nop":
            index += 1
        else:
            print("Dont know how to handle this", op)

    print("The accumulator ended at", accumulator)

    # ['nop', 'acc', 'jmp', 'acc', 'jmp', 'acc', 'acc', 'jmp', 'acc']
