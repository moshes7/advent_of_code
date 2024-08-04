import copy
import numpy as np


def process_text(data):

    num_list = []
    for row in data:

        first_digit = find_digit_string(row, invert=False)
        last_digit = find_digit_string(row, invert=True)

        num_str = f'{first_digit}{last_digit}'
        num = int(num_str)
        num_list.append(num)

        pass

    num_array = np.array(num_list)
    num_sum = num_array.sum()

    return num_sum



def test_1():

    input_file = 'input_example.txt'

    with open(input_file, 'r') as f:
        data = f.readlines()

    num_sum = process_text(data, replace_digit_str=False)

    assert num_sum == 142

    pass

def sum_of_digits():

    input_file = 'input.txt'

    with open(input_file, 'r') as f:
        data = f.readlines()

    num_sum = process_text(data, replace_digit_str=False)

    print(num_sum)

    pass

def replace_digit_string(str_in):

    replace_dict = {'one': '1',
                    'two': '2',
                    'three': '3',
                    'four': '4',
                    'five': '5',
                    'six': '6',
                    'seven': '7',
                    'eight': '8',
                    'nine': '9',
                    }

    str_out = str_in

    for key, val in replace_dict.items():
        str_out = str_out.replace(key, val)

    return str_out

def find_digit_string(str_in, invert=False):

    str_to_find_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '9',
                        '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
    str_to_find_list = list(str_to_find_dict.keys())

    if invert:
        str_in = str_in[::-1]
        str_to_find_list = [s[::-1] for s in str_to_find_list]

    min_ind = 1e7
    first_digit = None
    for str_to_find in str_to_find_list:

        ind = str_in.find(str_to_find)

        if (ind > -1) and (ind < min_ind):
            min_ind = ind
            key = str_to_find[::-1] if invert else str_to_find
            first_digit = str_to_find_dict[key]

        pass

    return first_digit


def test_1_part_2():

    input_file = 'input_example_part_2.txt'

    with open(input_file, 'r') as f:
        data = f.readlines()

    num_sum = process_text(data)

    assert num_sum == 281

def sum_of_digits():

    input_file = 'input.txt'

    with open(input_file, 'r') as f:
        data = f.readlines()

    num_sum = process_text(data)

    print(num_sum)

    pass


if __name__ == '__main__':

    # test_1()
    sum_of_digits()
    # test_1_part_2()

    pass