
def size(cms):
    if cms <= 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

#Function to encapsulate assertions

def size_check(length_in_cm, size_id):
    assert(size(length_in_cm) == size_id)

if __name__ == '__main__':
    size_check(37, 'S')
    size_check(40, 'M')
    size_check(43, 'L')
    size_check(38, 'S')
    print("All is well (maybe!)\n")
