import board
# Column major order
tiles = [
    "00:00", "01:01", "02:02", "03:03",
    "10:04", "11:05", "12:06", "13:07",
    "20:08", "21:09", "22:10", "23:11",
    "30:12", "31:13", "32:14", "33:15"
]

col1 = ["A", "B", "C", "D"]
col2 = ["E", "F", "G", "H"]
col3 = ["I", "J", "K", "L"]
col4 = ["M", "N", "O", "P"]

size = 4

col_idx = [range(i, size*size, size) for i in range(size)]
row_idx = [range(i*size, i*size+size) for i in range(size)]

for r in row_idx:
    for i in r:
        print(i, end = " ")
    print("")

print("------")

for c in col_idx:
    for i in c:
        print(i, end = " ")
    print("")

print("------")

r = col_idx[1]
print([tiles[i] for i in r])
print([tiles[i] for i in reversed(r)])


print("----------")
print("rows and columns in normal order:")
rows = [[tiles[i] for i in r] for r in row_idx]
cols = [[tiles[i] for i in c] for c in col_idx]
print(rows)
print(cols)
print("-----------")
print("rows and columns in reversed order:")
rows_rev = [[tiles[i] for i in reversed(r)] for r in row_idx]
cols_rev = [[tiles[i] for i in reversed(c)] for c in col_idx]
print(rows_rev)
print(cols_rev)


# Try to create new_tiles s.t. it uses col1, col2, etc as the new columns.
# That is: new_tiles = [A, E, I,...,B,F,J,...] etc.
new_tiles = [0]*size*size
for i,c_j in enumerate(col_idx[0]):
    new_tiles[c_j] = col1[i]
for i,c_j in enumerate(col_idx[1]):
    new_tiles[c_j] = col2[i]

print(new_tiles)

print(tiles())