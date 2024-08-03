import copy
import numpy as np


def process_text(data, replace_digit_str=False):

    num_list = []
    for row in data:

        if replace_digit_str:
            row = replace_digit_string(row)

        chars = list(row)
        digits = [c for c in chars if c.isdigit()]
        num_str = f'{digits[0]}{digits[-1]}'
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


def test_1_part_2():

    input_file = 'input_example_part_2.txt'

    with open(input_file, 'r') as f:
        data = f.readlines()

    num_sum = process_text(data, replace_digit_str=True)

    assert num_sum == 281



if __name__ == '__main__':

    # test_1()
    # sum_of_digits()
    test_1_part_2()

    pass