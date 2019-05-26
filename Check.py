from re import search
import sys

# check for valid input
def get_input_from_cmd(args_list):
    if len(args_list) != 2:
        raise Exception("Expected a 16-digit number as input argument")
    return args_list[1]

def is_input_valid(input_str):
    return bool(search(r"\d{16}", input_str))

#resolve 2 digit number conflict by adding the digits of the number and returning it
def sum_of_digits(num):
    num_list = convert_to_list(num)
    return sum(num_list)

#converts initial passed str variable to list
def convert_to_list(num):
    result = [int(x) for x in str(num)]
    return result


def main():
    input_string = get_input_from_cmd(sys.argv)
    if is_input_valid(input_string):
        digits_list = convert_to_list(input_string)
        card_valid =  card_check(digits_list)
        if card_valid:
            print('Valid Card!')
        else:
            print('Invalid Card!')
    else:
        print('Invalid Card Number!')

def card_check(digits_list, count = 0):
    if count % 2 == 0:
        digits_list[count] *= 2
        if digits_list[count] >= 10:
            digits_list[count] = sum_of_digits(digits_list[count])
    if count < 15:
        card_check(digits_list, count + 1)
    else:
        return 0
    result = bool(sum(digits_list)%10 == 0)
    return result

if __name__ == '__main__':
        main()
