from vector import Vector
import sys

list1 = [0.0, 1.0, 2.0, 3.0]
list2 = [[0.0], [1.0], [2.0], [3.0]]
list3 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
list4 = ["a", "b", "c"]

vec0 = Vector()
vec1 = Vector(list1)
vec2 = Vector(list2)
# vec3 = Vector(list3)
vec4 = Vector(3)
vec5 = Vector(range(10,15))
# vec6 = Vector(list4)

vectors = [vec0, vec1, vec2, vec4, vec5]

print("--- Vectors: ---")
for v in vectors:
    print(v)

print()

print("--- Additions: ---")
for v in vectors:
    res = v + v
    print(res)

res = vec0 + vec1
print(res)

print()

print("--- Substractions: ---")
for v in vectors:
    res = v - v / 2
    print(res)

print()

print("--- Multiplications: ---")
for v in vectors:
    res = v * 1.5
    print(res)

for v in vectors:
    res = 1.5 * v
    print(res)

print()

print("--- Divisions: ---")
for v in vectors:
    res = v / 2.0
    print(res)

print()

print("--- Dot Products: ---")
for v in vectors:
    w = v * 3
    print(w.dot(v))

print()

print("--- Transpose: ---")
for v in vectors:
    w = v
    print(w.T())
