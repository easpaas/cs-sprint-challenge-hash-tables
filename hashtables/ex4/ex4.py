def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    ht = {}

    # approach, add each negative number to dictionary as a key with value of true
    for negative in a:
        if negative < 0:
            ht[negative] = negative

    # compare each positive number to value in dict and append to result
    for num in a:
        # use of try/except to allow passing tests
        try:
            if ht[-num]:
                result.append(num)
        except:
            pass
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
