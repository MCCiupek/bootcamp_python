from vector import Vector
import sys

list1 = [0.0, 1.0, 2.0, 3.0]
list2 = [[0.0], [1.0], [2.0], [3.0]]
list3 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
list4 = ["a", "b", "c"]

try:
    vec0 = Vector()
    vec1 = Vector(list1)
    vec2 = Vector(list2)
    vec3 = Vector(list3)
    vec4 = Vector(3)
    vec5 = Vector(range(10,15))
    # vec6 = Vector(list4)
except ValueError as err:
    sys.stderr.write("Error: {0}\n".format(err))
    sys.exit()

vectors = [vec0, vec1, vec2, vec3, vec4, vec5]

print("--- Vectors: ---")
for v in vectors:
    try:
        print(v)
    except ValueError as err:
        sys.stderr.write("Error: {0}\n".format(err))

print()

print("--- Additions: ---")
for v in vectors:
    try:
        res = v + v
        print(res)
    except ValueError as err:
        sys.stderr.write("Error: {0}\n".format(err))

try:
    res = vec0 + vec1
    print(res)
except ValueError as err:
    sys.stderr.write("Error: {0}\n".format(err))

print()

print("--- Substractions: ---")
for v in vectors:
    try:
        res = v - v / 2
        print(res)
    except ValueError as err:
        sys.stderr.write("Error: {0}\n".format(err))

print()

print("--- Multiplications: ---")
for v in vectors:
    try:
        res = v * 1.5
        print(res)
    except ValueError as err:
        sys.stderr.write("Error: {0}\n".format(err))

for v in vectors:
    try:
        res = 1.5 * v
        print(res)
    except ValueError as err:
        sys.stderr.write("Error: {0}\n".format(err))

print()

print("--- Divisions: ---")
for v in vectors:
    try:
        res = v / 2.0
        print(res)
    except ValueError as err:
        sys.stderr.write("Error: {0}\n".format(err))

print()

print("--- Dot Products: ---")
for v in vectors:
    try:
        w = v * 3
        print(w.dot(v))
    except ValueError as err:
        sys.stderr.write("Error: {0}\n".format(err))

print()

print("--- Transpose: ---")
for v in vectors:
    try:
        w = v
        print(w.T())
    except ValueError as err:
        sys.stderr.write("Error: {0}\n".format(err))
