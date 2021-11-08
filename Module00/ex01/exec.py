import sys

av = sys.argv[1:]
for x in range(len(av)):
    av[x] = av[x][::-1].swapcase()
av.reverse()
print(*av, sep=' ')