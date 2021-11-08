import sys
import string

if len(sys.argv) != 3:
    sys.exit("ERROR")

s = sys.argv[1]

try:
    n = int(sys.argv[2])
except ValueError:
    sys.exit("ERROR")

if n < 0 or s.isdigit():
    sys.exit("ERROR")

s = s.translate(str.maketrans('', '', string.punctuation))
words = s.split()

filtered_list = [word for word in words if len(word) > n]

print(filtered_list)
