
MAJOR_COLORS = ["White", "Red", "Black", "Yellow", "Violet"]
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]


def get_color_from_pair_number(pair_number):
    major_index = pair_number // len(MINOR_COLORS)
    minor_index = pair_number % len(MINOR_COLORS)
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def print_color_map():
    for i in range(5):
        for j in range(5):
            pair_number = i * 5 + j
            print(f'{pair_number} | {get_color_from_pair_number(pair_number)[0]} | {get_color_from_pair_number(pair_number)[1]}')

print_color_map()

#asserting for each color pair
assert(get_color_from_pair_number(1) == ('White', 'Blue'))
assert(get_color_from_pair_number(2) == ('White', 'Orange'))
assert(get_color_from_pair_number(3) == ('White', 'Green'))
assert(get_color_from_pair_number(4) == ('White', 'Brown'))
assert(get_color_from_pair_number(5) == ('White', 'Slate'))
assert(get_color_from_pair_number(6) == ('Red', 'Blue'))
assert(get_color_from_pair_number(7) == ('Red', 'Orange'))
assert(get_color_from_pair_number(8) == ('Red', 'Green'))
assert(get_color_from_pair_number(9) == ('Red', 'Brown'))
assert(get_color_from_pair_number(10) == ('Red', 'Slate'))
assert(get_color_from_pair_number(11) == ('Black', 'Blue'))
assert(get_color_from_pair_number(12) == ('Black', 'Orange'))
assert(get_color_from_pair_number(13) == ('Black', 'Green'))
assert(get_color_from_pair_number(14) == ('Black', 'Brown'))
assert(get_color_from_pair_number(15) == ('Black', 'Slate'))
assert(get_color_from_pair_number(16) == ('Yellow', 'Blue'))
assert(get_color_from_pair_number(17) == ('Yellow', 'Orange'))
assert(get_color_from_pair_number(18) == ('Yellow', 'Green'))
assert(get_color_from_pair_number(19) == ('Yellow', 'Brown'))
assert(get_color_from_pair_number(20) == ('Yellow', 'Slate'))
assert(get_color_from_pair_number(21) == ('Violet', 'Blue'))
assert(get_color_from_pair_number(22) == ('Violet', 'Orange'))
assert(get_color_from_pair_number(23) == ('Violet', 'Green'))
assert(get_color_from_pair_number(24) == ('Violet', 'Brown'))
assert(get_color_from_pair_number(25) == ('Violet', 'Slate'))
print("All is well (maybe!)\n")
