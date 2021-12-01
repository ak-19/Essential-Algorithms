def create_subset(array):
    subset = [0]
    for x in array:
        new_subset = [x for x in subset]
        for s in subset:
            new_subset.append(s+x)
        subset = new_subset
    return subset


print(create_subset([1,2,3]))