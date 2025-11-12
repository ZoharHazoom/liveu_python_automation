# Concept
# Functions that yield values lazily — memory-efficient & great for pipelines.

# Example
# def count_to_three():
#     for i in range(1, 4):
#         yield i
#
#
# for num in count_to_three():
#     print(num)


def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


print(list(fib(20)))


# Exercise: make a generator that yields only even Fibonacci numbers.
def even_fib_numbers(limit):
    a, b = 0, 1
    while a < limit:
        if a % 2 == 0:
            yield a
        a, b = b, a + b


print(list(even_fib_numbers(20)))
