def swipe(line):
    left = []
    right = []
    active = None
    zeroes = 0
    for element in reversed(line):
        if element == 0:
            left.append(0)
            zeroes += 1
        elif None is active:
            active = element
        elif element is active:
            right = [element+1] + right
            active = None
            left.append(0)
            zeroes += 1
        elif element is not active:
            right = [active] + right
            active = element
    if active is not None:
        right = [active] + right
    return zeroes, left + right


class Board:
    def __init__(self, size):
        self.size = size
        self.tiles = [0]*size*size
        # randomize first tiles

    def _get_tile(self,row, column):
        # Column major order
        index = self.size*column + row
        return self.tiles(index)


    def swipe_right(self):
        for i in range(self.size):
            self.tiles[i]


