# find all unique elements in a string using the fact that sets contain unique elements
# https://medium.com/python-pandemonium/https-medium-com-python-pandemonium-an-introduction-to-python-sets-part-i-120974a713be

original_string = "aaabbbbaaccccddeeeeffffb"

# convert to set
the_set = set(original_string)

# join the set elements to form the string with unique elements
unique_string = ''.join(the_set)

print(unique_string)