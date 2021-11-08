from datetime import datetime

t = (3, 30, 2019, 9, 25)
# print("{3:0>2}/{4:0>2}/{2} {0:0>2}:{1:0>2}".format(*t))
print('{:%m/%d/%Y %H:%M}'.format(datetime(t[2], t[3], t[4], t[0], t[1])))
