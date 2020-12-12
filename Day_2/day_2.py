import re
from operator import xor

puzzle_input = []
READ_PUZZLE_INPUT = '(\d*)-(\d*)\s(\S):\s(\S*)'
file = open('puzzle_input.txt')
lines = file.read().split('\n')


def isValidPolicyOne(minimum_chars, maximum_chars, required_char, password):
    if password.count(required_char) >= int(minimum_chars):
        if password.count(required_char) <= int(maximum_chars):
            return True
        else:
            return False


def isValidPolicyTwo(first_position, second_position, required_char, password):
    if password[int(first_position) - 1] == required_char and password[int(second_position) - 1] != required_char:
        return True
    elif password[int(first_position) - 1] != required_char and password[int(second_position) - 1] == required_char:
        return True
    else:
        return False

#
# def policy_one(valid_passwords):
#     for line in lines:
#         puzzle_input.append(line)
#         p = re.compile(READ_PUZZLE_INPUT)
#         g = p.match(line)
#         minimum_chars = g.group(1)
#         maximum_chars = g.group(2)
#         required_char = g.group(3)
#         password = g.group(4)
#         validation = isValidPolicyOne(minimum_chars, maximum_chars, required_char, password)
#         if validation:
#             valid_passwords += 1
#         else:
#             pass
#     return valid_passwords


def policy_two(valid_passwords):
    for line in lines:
        puzzle_input.append(line)
        p = re.compile(READ_PUZZLE_INPUT)
        g = p.match(line)
        first_position = g.group(1)
        second_position = g.group(2)
        required_char = g.group(3)
        password = g.group(4)
        validation = isValidPolicyTwo(first_position, second_position, required_char, password)
        if validation:
            valid_passwords += 1
        else:
            pass
    return valid_passwords


#print("Valid passwords (first policy): ", policy_one(valid_passwords=0))
print("Valid passwords (second policy): ", policy_two(valid_passwords=0))
