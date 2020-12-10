from csv import reader

with open('input.txt', 'r') as read_obj:
    data_list = []
    csv_reader = reader(read_obj)
    for row in csv_reader:
        data_list.append(int(row[0]))

    counter1 = 0
    counter2 = counter1 + 1
    counter3 = counter2 + 1

    while counter1 < len(data_list) - 3:
        while counter2 < len(data_list) - 2:
            while counter3 < len(data_list) - 1:
                if ((data_list[counter1] + data_list[counter2] + data_list[counter3]) == 2020):
                    print("The answer is ", data_list[counter1], " * ", data_list[counter2], " * ", data_list[counter3], " = ", data_list[counter1] * data_list[counter2] * data_list[counter3])
                counter3 = counter3 + 1 # increment 
            counter2 = counter2 + 1 # increment 
            counter3 = counter2 + 1 # reset value 

        counter1 = counter1 + 1 # increment 
        counter2 = counter1 + 1 # reset value  
        counter3 = counter2 + 1 # reset value  
