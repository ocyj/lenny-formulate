import board
import random
# Column major order

tiles = [
    0,0,0,1,
    0,1,1,0,
    0,1,1,1,
    1,1,0,0
]
size = 4
col_idx = [range(i, size*size, size) for i in range(size)]
row_idx = [range(i*size, i*size+size) for i in range(size)]
print("--------")

zero_indices = []
for i, row in enumerate(row_idx):
    n_zeroes, swiped = board.swipe([tiles[j] for j in row])
    print(n_zeroes, swiped)
    zero_indices += row[0:n_zeroes]
new_zero = random.choice(zero_indices)
print(zero_indices, " choose ", new_zero)