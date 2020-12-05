# Our seat is defined as being the only empty seat (not in front, not in back)
def find_my_seat(seat_list):
    seat_list.sort()

    counter = 1
    while counter < len(seat_list) - 1:
        current_seat = seat_list[counter]
        next_seat = seat_list[counter + 1]

        if current_seat + 1 != next_seat:
            return current_seat + 1

        counter += 1

with open('input.txt', 'r') as read_obj:
    seat_list = []
    for row in read_obj:
        number_row = row.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0").strip()

        row = int(number_row[:7], 2)
        column = int(number_row[7:], 2)

        seat_id = row * 8 + column

        if seat_id not in seat_list:
            seat_list.append(seat_id)

    my_seat = find_my_seat(seat_list)
    print("My seat is", my_seat)
