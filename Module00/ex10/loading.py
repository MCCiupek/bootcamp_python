import time
import timeit
import sys


def ft_print_bar(j, i, width, size, elapsed_time):
    """Print progress bar"""
    percent = j / width
    eta = elapsed_time / percent * (1 - percent)
    s = "ETA: {0:.2f}s [{1: >2.0f}%][{2}] {3}/{4} | elapsed time {5:.2f}s"
    bar = s.format(eta,
                   percent * 100,
                   "=" * (j - 1) + ">" * (i != size) + " " * (width - j),
                   i,
                   size,
                   elapsed_time)
    sys.stdout.flush()
    sys.stdout.write("\r" + bar)
    sys.stdout.flush()


def ft_progress(listy, width=60):
    """Create and display a progress bar"""
    start = timeit.default_timer()
    size = len(listy)
    j = 0
    for i in listy:
        yield i
        if (i / size * width >= j + 1):
            j += 1
        ft_print_bar(j + 1, i + 1, width, size,
                     timeit.default_timer() - start)


# listy = range(1000)
# ret = 0
# for elem in ft_progress(listy):
#     ret += (elem + 3) % 5
#     time.sleep(0.01)
# print()
# print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)
