L = [1, 2, 3]
I = iter(L)
while True:
    try:
        print(next(I), sep='&')
    except StopIteration:
        print('list is done', end='')
        break

