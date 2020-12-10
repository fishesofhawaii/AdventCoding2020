# 3377 too low
# 4519 too high
def split(word): 
    return set([char for char in word])

with open('input.txt', 'r') as read_obj:
    is_first = True
    group_set = set()
    plane_answer_count = 0
    for row in read_obj:
        person_answer = row.strip()

        if len(person_answer) == 0:
            print(group_set)
            
            plane_answer_count += len(group_set)
            group_set = set()
            is_first = True
            continue

        person_set = split(person_answer)

        if is_first:
            group_set = person_set
            is_first = False
        else:
            group_set = group_set & person_set


    print(plane_answer_count)