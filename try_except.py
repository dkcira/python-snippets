# error handling using the try/except block
# useful to have 'else' for the case when no exception is raised

a,b = 1,0

try:
    print(a/b)
    # exception when b is 0
except ZeroDivisionError:
    print("division by 0")
else:
    print("no exceptions raised")
finally:
    print("Run this always")