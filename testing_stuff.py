def trim_zeroes(l):
    l = list(l)
    while len(l) > 0 and l[-1] == 0:
        l.pop()
    return l

def print_result(l):
    print('{} -> {}'.format(l, trim_zeroes(l)))

def main():
    a1 = [0, 1, 3, 2, 1, 0, 1, 0, 2, 0, 0, 0]
    a2 = [0, 0, 0, 0, 0]
    a3 = [0 ,1, 2, 3, 0, -1, 0, 0, 0]
    a4 = [0, 1, 0, 1, 2, 0] #[0, 0, 0, 0, 2, 2]

    print_result(a1)
    print_result(a2)
    print_result(a3)



if __name__ == '__main__':
    main()