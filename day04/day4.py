# Not happy with how this ended up. Definitely would refactor
def isPropertyValueValid(key, value):
    if key == "byr":
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        byr_val = int(value)
        return 1920 <= byr_val & byr_val <= 2002
    elif key == "iyr":
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        iyr_val = int(value)
        return 2010 <= iyr_val & iyr_val <= 2020
    elif key == "eyr":
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        eyr_val = int(value)
        return 2020 <= eyr_val & eyr_val <= 2030
    elif key == "hgt":
        # hgt (Height) - a number followed by either cm or in:
            # If cm, the number must be at least 150 and at most 193.
            # If in, the number must be at least 59 and at most 76.

        number_part = ""
        letter_part = ""

        for character in value:
            if character.isdigit():
                number_part += character
            else: 
                letter_part += character

        hgt_num = int(number_part)

        if letter_part == "cm":
            return 150 <= hgt_num & hgt_num <= 193
        elif letter_part == "in":
            return 59 <= hgt_num & hgt_num <= 76

        return False
    elif key == "hcl":
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if value[0] != "#":
            return False
        for l in value:
            if l not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "#"]:
                return False
        return True

    elif key == "ecl":
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return value in valid_ecl
    elif key == "pid":
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        return value.isnumeric() and len(value) == 9
    elif key == "cid":
        # cid (Country ID) - ignored, missing or not.
        return True
    else: 
        print("Unknown key", key)
        return False

def isPassportValid(passport):
    field_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    passport_data_list = passport.split(" ")

    for property_pair in passport_data_list:
        property_pair_key = property_pair.split(":")[0]
        property_pair_value = property_pair.split(":")[1]

        if not isPropertyValueValid(property_pair_key, property_pair_value):
            return False
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