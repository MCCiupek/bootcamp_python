import time
import timeit
import sys

def ft_progress(listy):
    start = timeit.default_timer()
    elapsed_time = timeit.default_timer() - start
    toolbar_width = 60
    size = len(listy)
    struct = "ETA: {0:.2f}s [{1: >2}%]".format(0, 0)
    sys.stdout.write("ETA: {0:.2f}s [{1: >2}%][{2}] {3}/{4} | elapsed time {5:.2f}s".format(0, 0," " * toolbar_width, 0, size, elapsed_time))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1+16*2-4))
    j = 0
    for i in listy:
        yield i
        elapsed_time = timeit.default_timer() - start
        if (i / size * toolbar_width > j + 1):
            j += 1
            sys.stdout.write(">")
            sys.stdout.write("\b")
            sys.stdout.write("=")
            sys.stdout.flush()
    sys.stdout.write("=\n")

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)

# listy = range(3333)
# ret = 0
# for elem in ft_progress(listy):
#     ret += elem
#     time.sleep(0.005)
# print()
# print(ret)