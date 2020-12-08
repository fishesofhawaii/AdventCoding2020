class Bag:
    def __init__(self, color, size):
        self.bags = []
        self.color = color
        self.size = size
   
    def add_bag(self, bag):
        self.bags.append(bag)

    def print(self, indent):
        print(" " * indent, self.color, self.size)

    def print_bags(self, depth = 0):
        for bag in self.bags:
            bag.print(depth)
            bag.print_bags(depth + 1)

    def find(self, color):
        for bag in self.bags:
            if bag.color == color:
                return bag
            else:
                return bag.find(color)

        return None
    
def find_bag(bags, color):
    for bag in bags.values():
        found_bag = bag.find(color)
        if found_bag != None:
            return found_bag
            
    return None

def get_bag_list(bags, raw_bag_string):
    bag_list = []
    if raw_bag_string == "no other bags":
        return bag_list

    raw_bag_list = raw_bag_string.split(",")
    
    for raw_bag in raw_bag_list:
        bag_string = raw_bag.strip()
        bag_data_list = bag_string.split(" ")

        assert bag_data_list[-1] in ["bag", "bags"] # Making sure input is as expected
        
        color_name = " ".join(bag_data_list[1:-1])
        
        bag = find_bag(bags, color_name)
        if bag == None:
            bag = Bag(color_name, int(bag_data_list[0]))

        # Need to try to find the bag
        bag_list.append(bag)

    return bag_list

with open('input.txt', 'r') as read_obj:
    bags = {}
    for row in read_obj:
        clean_row = row.strip()
        color_bag_count_split = clean_row.split("bags contain")
        
        # This should have 2 parts
        # Part 1: color (of the bag)
        # Part 2: CSV of more bag color and quantities

        color = color_bag_count_split[0].strip()
        input_bag = Bag(color, 1)
        raw_bag_string = color_bag_count_split[1].replace(".", "").strip()
        bag_list = get_bag_list(bags, raw_bag_string)

        for bag in bag_list:
            input_bag.add_bag(bag)

        was_added = False
        for bag in bags.values():
            found_bag = bag.find(input_bag.color)
            if found_bag != None:
                found_bag.add_bag(input_bag)
                was_added = True
        if not was_added:
            bags[color] = input_bag


    for bag in bags.values():
        bag.print_bags()