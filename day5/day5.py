with open('input.txt', 'r') as read_obj:

    highest_seat_id = 0
    for row in read_obj:
        number_row = row.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0").strip()
        
        row = int(number_row[:7], 2)
        column = int(number_row[8:], 2)

        seat_id = row * 8 + column

        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    print("The highest seat id from the list was", highest_seat_id)