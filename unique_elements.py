def sort_and_remove_duplicates(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    unique_elements = [0] * len(arr)
    index = 0
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            unique_elements[index] = arr[i]
            index += 1
    return unique_elements[:index]

# Test the function with an example array
arr = [5, 4, 7, 5, 1, 3, 4]
print("Given input -",arr)
print("Output -",sort_and_remove_duplicates(arr))