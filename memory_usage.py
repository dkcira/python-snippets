# check memory usage of an object using sys.getsizeof

import sys

original_string = "pasadena"

print(original_string + " has a size of",sys.getsizeof(original_string), "bytes")