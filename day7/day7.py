# INCOMPLETE
class Bag:
    def __init__(self, color, size):
        self.parent_bags = []
        self.color = color
        self.size = size
   
    def add_parent(self, parent):
        self.parent_bags.append(parent)

    def print_bag(self, depth = 0):
       print(" " * depth, "Color: {} Size: {}".format(self.color, self.size))

    def print_all(self, depth = 0):
        self.print_bag(depth)
        for parent in self.parent_bags:
            parent.print_all(depth + 1)

    def find_bag(self, color):
        if self.color == color:
            return self
        else: 
            for parent_bag in self.parent_bags:
                return parent_bag.find_bag(color)

        return None

    # def print_all(self, indent = 0):
    #     self.print_bag(indent)
    #     for parent in self.parent_bags:
    #         parent.print_all(indent + 1)
        
def get_bag_list(raw_bag_string):
    bag_list = []
    if raw_bag_string == "no other bags":
        return bag_list

    raw_bag_list = raw_bag_string.split(",")
    
    for raw_bag in raw_bag_list:
        bag_string = raw_bag.strip()
        bag_data_list = bag_string.split(" ")

        assert bag_data_list[-1] in ["bag", "bags"] # Making sure input is as expected
        
        color_name = " ".join(bag_data_list[1:-1])
        bag = Bag(color_name, int(bag_data_list[0]))

        bag_list.append(bag)

    return bag_list

def populate_bag_set(bag, bag_set):
    bag_set.add(bag.color)
    for parent in bag.parent_bags:
        populate_bag_set(parent, bag_set)

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
        bag_list = get_bag_list(raw_bag_string)

        for bag in bag_list:
            bag.add_parent(input_bag)
            bags[bag.color] = bag

    # a = Bag("a", 1)
    # b = Bag("b", 1)
    # c = Bag("c", 1)
    # d = Bag("d", 1)

    # a.add_parent(b)
    # b.add_parent(c)
    # c.add_parent(d)

    # bags["a"] = a

    # for bag in bags.values():
    #     bag.print_bags()