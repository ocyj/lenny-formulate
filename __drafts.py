import board
# Column major order
tiles = [
    "00:00", "01:01", "02:02", "03:03",
    "10:04", "11:05", "12:06", "13:07",
    "20:08", "21:09", "22:10", "23:11",
    "30:12", "31:13", "32:14", "33:15"
]

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
