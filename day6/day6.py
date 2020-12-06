def split(word): 
    return set([char for char in word])  


with open('input.txt', 'r') as read_obj:
    group_answers = set()
    plane_answers = []
    for row in read_obj:
        clean_row = row.strip()
        user_answers = split(clean_row)
        group_answers = group_answers | user_answers

        if len(clean_row) == 0:
            plane_answers.append(group_answers)
            group_answers = set()
            continue
        
    plane_answers.append(group_answers)

    counter = 0
    for group in plane_answers:
        counter += len(group)

    print("there were", counter, "answers")