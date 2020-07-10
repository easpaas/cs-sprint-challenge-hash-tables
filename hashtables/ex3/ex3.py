def intersection(arrays):
    """
    YOUR CODE HERE
    """
    ht = {}
    result = []

    # iterate through each sub list of integers 
    for subArr in arrays:
        for i in subArr:
            # does not already exist, set occurrence to 1
            if i not in ht:
                ht[i] = 1
            else:
                ht[i] += 1
                if ht[i] == len(arrays):
                    result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
