def arraySortedOrNot(arr, n):
    # Base case
    if n == 0 or n == 1:
        return True

    # Check if present index and index previous to it are in correct order
    # and rest of the array is also sorted
    # If true, then return true; else return false
    return (arr[n - 1] >= arr[n - 2] and arraySortedOrNot(arr, n - 1))
