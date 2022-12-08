#Day01 - Part 2

temp = 0
cal01 = 0
cal02 = 0
cal03 = 3
final = 0

with open('day01/input.txt') as input_file:
    for line in input_file:
        if len(line) > 1:
         temp = temp + int(line)
        else:
            if temp > cal01:
                cal01 = temp
            elif temp > cal02:
                cal02 = temp
            elif temp > cal03:
                cal03 = temp 
            temp = 0
final = cal01 + cal02 + cal03
print(final)