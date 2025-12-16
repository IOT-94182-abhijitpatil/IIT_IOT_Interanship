def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


# Example usage
l1 = [1, 2, 3, 4]
l2 = [5, 6, 8, 3]

print(overlapping(l1, l2))
