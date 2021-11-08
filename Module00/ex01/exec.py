import sys

av = sys.argv[1:]
av = [av[x][::-1].swapcase() for x in range(len(av))]
av.reverse()
print(*av, sep=' ')