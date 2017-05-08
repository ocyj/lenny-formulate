column major order

```python
'''
00:00 01:04 02:08 03:12
10:01 11:05 12:09 13:13
20:02 21:06 22:10 23:14
30:03 31:07 32:11 33:15
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
      if 0 <= i and i <= size - 1:
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

Om man swajpar nedåt, kommer en av raderna (eg kolumnerna) ju vara ex [01, 11, 21, 31] som swajpas så att 31 är sista elementet. Ponera att swipe-funktionen returnerar 2 antal nollor (ex, den swajpade raden skulle kunna vara [0, 0, 1, 2]). Hur mappa 2 till elementindexen 01 och 11, vilka i den egentliga tileslistan har index 4, 5?

behöver en funktion av typen get_zero_indices(n_zeros, column_idx)

som vid anrop returnerar

----------

```python
import random
random.choices(sequence) # returnerar ett element från sequence.
#Bra för att slumpa fram var nya elementet skall läggas in!
```
