
MAJOR_COLORS = ["White", "Red", "Black", "Yellow", "Violet"]
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]


def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def print_color_map():
    for i in range(5):
        for j in range(5):
            pair_number = i * 5 + j +1 #1 is added to account for zero error as list index begins with 0
            print(f'{pair_number} | {get_color_from_pair_number(pair_number)[0]} | {get_color_from_pair_number(pair_number)[1]}')

print_color_map()

def test_color_map(test_paid_number, expected_major_colour, expected_minor_color):
    assert(get_color_from_pair_number(test_paid_number) == (expected_major_colour, expected_minor_color))
    
    

#testing each of 25 color pairs
if __name__ == '__main__':
    print_color_map()
    test_color_map(1, 'White', 'Blue')
    test_color_map(2, 'White', 'Orange')
    test_color_map(3, 'White', 'Green')
    test_color_map(4, 'White', 'Brown')
    test_color_map(5, 'White', 'Slate')
    test_color_map(6, 'Red', 'Blue')
    test_color_map(7, 'Red', 'Orange')
    test_color_map(8, 'Red', 'Green')
    test_color_map(9, 'Red', 'Brown')
    test_color_map(10, 'Red', 'Slate')
    test_color_map(11, 'Black', 'Blue')
    test_color_map(12, 'Black', 'Orange')
    test_color_map(13, 'Black', 'Green')

    print("All is well (maybe!)\n")
