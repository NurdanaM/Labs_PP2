def uniqueElements(lst):
    unique_list = []
    for l in lst:
        if l not in unique_list:
            unique_list.append(l)

    return unique_list

nums = [1, 2, 3, 3, 4, 5, 6, 6, 7]
print(uniqueElements(nums))
