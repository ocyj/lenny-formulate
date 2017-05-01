import line

# a = [0, 1, 3, 2, 1,0,1,0,2,0,0,0]
a = [0, 0, 0, 0, 0]
print(a)


def trim_zeroes(l):
    while len(l) > 0 and l[-1] == 0:
        l.pop()
    return l


print(trim_zeroes(a))

print(line.lol())
