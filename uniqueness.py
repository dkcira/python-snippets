# check if all elements of a list are unique or not

def unique(l):
    if len(l) == len(set(l)):
        print("all elements are unique")
    else:
        print("list has duplicates")

unique([1,2,3,4])
unique([1,1,2,3])