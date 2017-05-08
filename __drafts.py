# Column major order
tiles = [
    "00:00", "10:01", "20:02", "30:03",
    "01:04", "11:05", "21:06", "31:07",
    "02:08", "12:09", "22:10", "32:11",
    "03:12", "13:13", "23:14", "33:15"
]

size = 4

row_idx = [range(i, size*size, size) for i in range(size)]
col_idx = [range(i*size, i*size+size) for i in range(size)]

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

