# # squares of even numbers
# nums = [1, 2, 3, 4, 5, 6]
# evens_sq = [n**2 for n in nums if n % 2 == 0]
# print(evens_sq)  # [4, 16, 36]
#
# # word lengths dictionary
# words = ["liveu", "stream", "automation"]
# lengths = {w: len(w) for w in words}
# print(lengths)
#
# # flatten 2D list
# matrix = [[1,2,3],[4,5,6]]
# flat = [x for row in matrix for x in row]
# print(flat)


# Drill 1 make a list of (num, num**3) for odd numbers ≤ 10
res = [(num, num**3) for num in range(1, 11) if num % 2 == 1]
print(res)


# Create a list of squares only for numbers divisible by 3, up to 20.
res = [num ** 2 for num in range(1, 21) if num & 3 == 0]
print(res)

# Build a dictionary where keys are letters, and values are
# their positions in the alphabet, but only for vowels (a, e, i, o, u).
vowels = 'aeiou'
alphabet_dict = {ch: ord(ch) - 96 for ch in vowels}
print(alphabet_dict)

# Flatten a 2D matrix, but only take even numbers.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [x for row in matrix for x in row if x % 2 == 0]
print(result)


