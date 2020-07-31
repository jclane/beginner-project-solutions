

def count_animals(heads, legs, count):
    while not (2 * count) + (4 * (heads - 1)) == legs:
        return count_animals(heads - 1, legs, count + 1)
    return count, heads - 1


print(count_animals(36, 94, 0))
