def isPasswordValid(password, letter, minimum, maximum):
    occurrences = 0
    for l in password: 
        if letter == l:
            occurrences = occurrences + 1

    print(occurrences, maximum, minimum)

    if occurrences >= int(minimum) and occurrences <= int(maximum):
        return True

    return False


with open('input.txt', 'r') as read_obj:
    rule_list = [] # EX: 1-13 b
    pass_list = [] # EX: bbbbbbbbbb

    for row in read_obj:
        rule_pass_list = row.split(":")
        rule_list.append(rule_pass_list[0])
        pass_list.append(rule_pass_list[1])

    counter = 0
    valid_password_counter = 0
    while counter < len(rule_list):
        raw_rule_data = rule_list[counter]
        rule_data_split = raw_rule_data.split(" ")

        numbers_raw = rule_data_split[0] # EX: 1-13
        numbers_split = numbers_raw.split("-")

        min_num = numbers_split[0] # EX: 1
        max_num = numbers_split[1] # EX: 13

        rule_letter = rule_data_split[1] # EX: b

        pass_string = pass_list[counter]

        if isPasswordValid(pass_string, rule_letter, min_num, max_num): 
            valid_password_counter = valid_password_counter + 1



        counter = counter + 1

    print("We found", valid_password_counter, "valid passwords")

