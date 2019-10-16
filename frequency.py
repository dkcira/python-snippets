# count frequency of elements in a list using the Counter class in the collections module

from collections import Counter

original_list = ['a','a','a','a','b','b','c','d','d','d','d','d']

count = Counter(original_list)

# print all counts
print("all counts: ",count)

# print counts of an element
print("frequency of 'a': ",count['a'])

# print most frequent element
print("most frequent element: ",count.most_common(1))