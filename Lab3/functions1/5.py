import itertools

def func():
    s = input("Enter a string: ")

    permutations = itertools.permutations(s)

    for perm in permutations:
        print("".join(perm))

func()