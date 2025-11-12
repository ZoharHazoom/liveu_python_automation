data = [{'name':'a','age':25},{'name':'b','age':19}]
print(sorted(data, key=lambda d: d['age']))

from itertools import groupby
nums = [1,1,2,2,3,3,3,4]
for k, g in groupby(nums):
    print(k, list(g))
