def swipe(line, return_zeroes = True):
    left = []
    right = []
    active = None
    zeroes = 0
    collapsed = False
    for element in reversed(line):
        if element == 0:
            left.append(0)
            zeroes += 1
        elif None is active:
            active = element
        elif element is active:
            collapsed = True
            right = [element+1] + right
            active = None
            left.append(0)
            zeroes += 1
        elif element is not active:
            right = [active] + right
            active = element
    if active is not None:
        right = [active] + right
    # if collapsed or not(zeroes == len(line)) --> line changed!
    if return_zeroes:
        return zeroes, left + right
    return left + right


class Board:
    def __init__(self, size):
        self.size = size
        self.tiles = [0]*size*size

        # uses row major order
        #             eg [0, 4, 8, 12], [1, 5, 9, 13], ...
        self.col_idx = [range(i, size*size, size) for i in range(size)]

        #             eg [0, 1, 2, 3], [4, 5, 6, 7], ...
        self.row_idx = [range(i*size, i*size+size) for i in range(size)]

        # TODO: randomize first tiles

    def swipe_down(self):
        columns = self.col_idx
        self._swipe_board(columns)

    def swipe_up(self):
        columns = reversed(self.col_idx)
        self._swipe_board(columns)

    def swipe_right(self):
        rows = self.row_idx
        self._swipe_board(rows)

    def swipe_left(self):
        rows = reversed(self.row_idx)
        self._swipe_board(rows)

    def _swipe_board(self, lines):
        same_board = True
        empty_tiles_indices = []
        for line in lines:
            old_line = [self.tiles[j] for j in line]
            n_zeroes, new_line = swipe(old_line)
            if old_line != new_line:
                same_board = False
            empty_tiles_indices += line[0:n_zeroes]
            self._update_tiles(new_line, line)

        if len(empty_tiles_indices) is 1:
            # TODO: implement Game over
            pass
        elif same_board:
            pass # Do nothing
        else:
            # Normal case, add new tile = 1,2 w 10,90% prob resp.
            # TODO
            pass



    def _update_tiles(self, new_tiles, indices):
        for index_value in zip(indices, new_tiles):
            i,v = index_value
            self.tiles[i] = v

    def __str__(self):
        rep = ""
        for r in self.row_idx:
            l = map(str, [self.tiles[i] for i  in r])
            rep += "  ".join(l) + "\n"
        return rep

if __name__ == "__main__":
    b = Board(size=4)
    b.tiles = [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1]
    print(b)
    b.swipe_down()

