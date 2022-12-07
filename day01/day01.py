#Day01 - Part 1

final = 0
temp = 0

with open('input.txt') as input_file:
    for line in input_file:
        if len(line) > 1:
         temp = temp + int(line)
        else:
            if temp > final:
                final = temp
            temp = 0
print(final)
