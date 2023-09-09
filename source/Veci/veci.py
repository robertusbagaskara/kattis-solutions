import itertools

if __name__ == "__main__":
    x = int(input())
    resource = [*str(x)]
    num = 0
    permutations = list(itertools.permutations(resource))
    permutations.sort()
    for permutation in permutations:
        comparer = "".join(permutation)
        if int(comparer) > x:
            num = int(comparer)
            break
    print(num)