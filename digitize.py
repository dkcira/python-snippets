# convert integer into list of digits

num = 123456

# using map
list_of_digits = list(map(int, str(num)))
print(list_of_digits)

# using list comprehension
list_of_digits = [int(x) for x in str(num)]
print(list_of_digits)