# flatten a list of lists

from iteration_utilities import deepflatten

# use this simple function for one-depth nested list
def flatten(l):
    return [item for sublist in l for item in sublist]

l = [[1,2,3],[4]]
print(flatten(l))

# use the deepflatten method from iteration_utilities if more nested list
nested = [[1,2,3],[4,[5],[6,7]],[8,[9,[10]]]]
print(list(deepflatten(nested, depth=3)))