# measure time it takes code to execute

import time
start = time.time()

# begin code
a,b = 1,2
c = a + b
# end code

end = time.time()

length_in_microseconds = (end - start)*(10**6)

print(f"The time taken is {length_in_microseconds} \u03BCs")


