A = 
B = 
C = 
X = 1
Y = 2
Z = 3
score = 0

with open('input-2.txt') as input_file:
    for line in input_file:
        if line[0] == 'A' & line[2] == 'X':
            score = score + 1 + 3
        elif line[0] == 'A' & line[2] == 'Y':
            score = score + 2 + 6
        elif line[0] == 'A' & line[2] == 'Z':
            score = score + 3 + 0
        elif line[0] == 'B' & line[2] == 'X':
            score = score + 1 + 0
        elif line[0] == 'B' & line[2] == 'Y':
            score = score + 2 + 3  
        elif line[0] == 'B' & line[2] == 'Z':
            score = score + 3 + 6
        elif line[0] == 'C' & line[2] == 'X':
            score = score + 1 + 6
        elif line[0] == 'C' & line[2] == 'Y':
            score = score + 2 + 0
        elif line[0] == 'C' & line[2] == 'Z':
            score = score + 3 + 0
print(score)
