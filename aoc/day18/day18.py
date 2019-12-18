matrix = [list(line.strip("\n")) for line in open('input.txt').readlines()]

at_start = None

print(matrix[0][0], type(matrix[0][0]))
keys = {}
doors = {}

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == '@':
            at_start = (row, col)
        elif 97 <= ord(matrix[row][col]) < 123:
            keys[matrix[row][col]] = (row, col)
        elif 65 <= ord(matrix[row][col]) < 91:
            doors[matrix[row][col]] = (row, col)

print(f'start = {at_start}')  # 40, 40
print(keys)
print(doors)
