filepath = 'puzzle_input.txt'
puzzle_input = []

file = open('puzzle_input.txt')
lines = file.read().split('\n')
for line in lines:
    puzzle_input.append(line)
puzzle_input[:] = list(map(int, puzzle_input))
print(puzzle_input)

for i,n1 in enumerate(puzzle_input):
    for j, n2 in enumerate(puzzle_input[i+1:]):
        if n1 + n2 == 2020:
            part1 = n1*n2
        for n3 in puzzle_input[i+j+1:]:
            if n1 + n2 + n3 == 2020:
                part2 = n1*n2*n3
print(part1)
print(part2)


# def add_elements_from_a_list(a, b):
#     result = puzzle_input[a] + puzzle_input[b+1]
#     print(puzzle_input[a], '+', puzzle_input[b+1], '=', (result))
#     return result

# counter = 0
# for i in range(len(puzzle_input[0:-1])):
#     # result = puzzle_input[counter] + puzzle_input[i+1]
#     result = add_elements_from_a_list(counter, i)
#     # print(puzzle_input[counter], '+', puzzle_input[i+1])
#     while result != 2020:
#         print(counter)
#         counter = counter + 1
#         result = add_elements_from_a_list(counter, i)
#     else:
#         print(puzzle_input[counter], '+', puzzle_input[i+1], ' = 2020')
        