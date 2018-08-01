import board
import random


def main():
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


def update_tiles(new_tiles, indices):
    col_idx = [1, 5, 9, 13]
    new_col = [11, 22, 33, 44]
    tiles_before   = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    tiles_desired  = [0, 11, 0, 0, 0, 22, 0, 0, 0, 33, 0, 0, 0, 44, 0, 0]

    tiles_after = list(tiles_before)
    for ind_val in zip(col_idx, new_col):
        # id_val is a tuple such as (1, a) or (5, b) etc.
        i, v = ind_val
        tiles_after[i] = v

    print(tiles_before)
    print(tiles_after)
    print(tiles_desired)

if __name__ == '__main__':
    main2()
