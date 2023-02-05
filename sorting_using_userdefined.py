def check_ele(arr):
    frequency = {}
    for i in arr:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    for key, value in frequency.items():
        if value > 1:
            print("frequency of ", key, "element is -", value)

def find_duplicates(arr):
    check_ele(arr)

arr = [2, 3, 1, 2, 5, 7, 2, 3, 5]
find_duplicates(arr)
