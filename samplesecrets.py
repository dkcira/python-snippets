# use the secrets library for generating random samples for cryptography purposes
# https://docs.python.org/3/library/secrets.html

import secrets                         # secure module
secure_random = secrets.SystemRandom() # secure random object

original_list = ['a','b','c','d','e','f','g']

num_samples = 3

samples = secure_random.sample(original_list, num_samples)

print(samples)