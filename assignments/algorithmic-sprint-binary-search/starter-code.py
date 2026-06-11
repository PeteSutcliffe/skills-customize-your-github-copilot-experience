def binary_search(arr, target):
    """Return index of target in sorted list arr, or -1 if not found."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def two_pointer_pair_sum(arr, target):
    """Assumes arr is sorted. Return tuple of indices (i, j) or None."""
    i, j = 0, len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            return (i, j)
        if s < target:
            i += 1
        else:
            j -= 1
    return None


if __name__ == "__main__":
    # Binary search tests
    assert binary_search([1, 2, 3, 4, 5], 4) == 3
    assert binary_search([1, 2, 3], 7) == -1

    # Two-pointer tests
    assert two_pointer_pair_sum([1, 2, 3, 4, 6], 6) == (1, 3)
    assert two_pointer_pair_sum([1, 2, 3], 7) is None

    print("Starter code tests passed")
