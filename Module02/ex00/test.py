from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

# Example 0: subject:
x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
#   Output:
#   <generator object ft_map at 0x7f708faab7b0> # The adress will be different

print(list(ft_map(lambda t: t + 1, x)))
#   Output:
#   [2, 3, 4, 5, 6]


# Example 1: Working of map()
def calculateSquare(n):
    return n*n


numbers = (1, 2, 3, 4)
result = ft_map(calculateSquare, numbers)
print(result)

numbersSquare = set(result)
print(numbersSquare)

#   Output
#   <generator object ft_map at 0x7f722da129e8>
#   {16, 1, 4, 9}

# Example 2: How to use lambda function with map()?
numbers = (1, 2, 3, 4)
result = ft_map(lambda x: x*x, numbers)
print(result)

#   converting map object to set
numbersSquare = set(result)
print(numbersSquare)

#   Output
#   <generator object ft_map at 0x7fafc21ccb00>
#   {16, 1, 4, 9}

# Example 3: Passing Multiple Iterators to map() Using Lambda
# num1 = [4, 5, 6]
# num2 = [5, 6, 7]

# result = ft_map(lambda n1, n2: n1+n2, num1, num2)
# print(list(result))

#   Output
#   [9, 11, 13]

# Example 4: Passing non-iterable object as argument
result = ft_map(lambda x: x*x, 1)
print(result)

# Example 5: Passing iterable that can not be used by the function

letters = ['a', 'b', 'c']
result = ft_map(str.upper, letters)

print(result)
print(list(result))

# numbers = (1, 2, 3, 4)
# result = ft_map(str.upper, numbers)

# print(result)
# print(list(result))

# -----------------------------------------------

# Example 2:
print(ft_filter(lambda dum: not (dum % 2), x))
# Output:
# <generator object ft_filter at 0x7f709c777d00> # The adress will be different

print(list(ft_filter(lambda dum: not (dum % 2), x)))
# Output:
# [2, 4]


# Example 3:
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
# Output:
# "Hello world"
