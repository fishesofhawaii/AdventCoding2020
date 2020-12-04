def isPassportValid(passport):
    field_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    passport_data_list = passport.split(" ")

    for property_pair in passport_data_list:
        property_pair_key = property_pair.split(":")[0]
        if property_pair_key in field_list:
            field_list.remove(property_pair_key)

    if (len(field_list) == 0) | (len(field_list) == 1 & ("cid" in field_list)):
        return True

    return False


with open('input.txt', 'r') as read_obj:
    passport_string_list = []

    passport_string = ""
    for row in read_obj:
        clean_row = row.strip()

        if len(clean_row) == 0: # Empty row indicates the end of a passport data set
            passport_string_list.append(passport_string.strip())
            passport_string = ""
            continue

        passport_string = passport_string + " " + clean_row

    # Last passport in list
    passport_string_list.append(passport_string.strip())

    valid_counter = 0
    invalid_counter = 0
    for passport in passport_string_list:
        is_valid = isPassportValid(passport)

        if is_valid:
            valid_counter += 1
        else: 
            invalid_counter += 1

    print("There were", valid_counter, "valid passports")
    print("There were", invalid_counter, "invalid passports")