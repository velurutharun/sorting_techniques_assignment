def count_duplicates(arr):
    arr.sort()
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    duplicate_count = {k: v for k, v in count.items() if v > 1}
    return duplicate_count

# Test the function with an example array
arr = [2, 3, 1, 2, 5, 7, 2, 3, 5]
duplicates = count_duplicates(arr)
for num, frequency in duplicates.items():
    print(f"frequency of {num} element is - {frequency}.")