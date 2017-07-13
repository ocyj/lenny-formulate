column major order

```python
'''
# Row major order:
"00:00", "01:01", "02:02", "03:03",
"10:04", "11:05", "12:06", "13:07",
"20:08", "21:09", "22:10", "23:11",
"30:12", "31:13", "32:14", "33:15"
'''
#         0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15   
tiles = [00, 10, 20, 30, 01, 11, 21, 31, 02, 12, 22, 32, 03, 13, 23, 33]
```

```python
def row(self, i):
  if 0 <= i and i <= size - 1:
    return tiles[i:size*size:size]
```

```python
def col(self,j):
      if 0 <= i and i <= size - 1:8
        return tiles[j*size:j*size + size]
```

```python
def get_cols_increasing:
  l = []
  for i in range(self.size):
    l = l + self.row(i)
    #W will return
```

```python
def get_cols_decreasing(self):
  l = []
  for i in reversed(range(self.size))
```

### pseudo code for a swipe_command
```
same_board = True
empty_tiles_indices = []
# row is an iterable with indices for tiles for that row.
# the order in row or column depends if its a right/left or up/down swipe
for each row/(column) in rows/(columns)
    old_line = [tiles[j] for j in row] 
    n_zeroes, new_line = swipe(old_line)
    if old_line != new_line:
        same_board = False
    # Add position of empty tiles in new board to list
    empty_tiles_indices += row[0:n_zeroes]
    update_tiles(new_line, row)
    
if len(empty_tiles_indices) is 1:
    # Game over!
elif same_board:
    # Don't insert new tile. Let user swipe again
elif:
    # Normal case: insert a new tile = 1/2 with 90/10% probability in randomly
    #  picked position in empty_tiles_indices.
        
```    


Write tests! e.g.
```python
        b = board.Board(4)
        tiles_before = [0]*16
        tiles_expected = [0, 0]
        new_tiles = range(4)
        indices = [1, 5, 9, 13]

        b.update_tiles()
```


```python
import random
random.choices(sequence) # returnerar ett element från sequence.
#Bra för att slumpa fram var nya elementet skall läggas in!
```
