def smallest_missing_positive(A):
    # Convert the array to a set for fast lookups
    num_set = set(A)

    # Start checking from 1 upwards
    smallest_positive = 1

    while smallest_positive in num_set:
        smallest_positive += 1
        # print(smallest_positive)

    print(smallest_positive)


# Test cases
print(smallest_missing_positive([1, 3, 6, 4, 1, 2]))  # Output: 5
print(smallest_missing_positive([1, 2, 3]))  # Output: 4
print(smallest_missing_positive([-1, -2]))