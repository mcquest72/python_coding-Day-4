
# A Matrix program using nested list

print()

row1 = ['😉', '😉', '😉']
row2 = ['😉', '😉', '😉']
row3 = ['😉', '😉', '😉']

map = [row1, row2, row3]

print(f'{row1}\n{row2}\n{row3}')

print()
position = input('Where do you want to put the treasure?\n')
print()

horizonal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical -1]
selected_row[horizonal -1] = 'X'
print()

print(f'{row1}\n{row2}\n{row3}')
print()
