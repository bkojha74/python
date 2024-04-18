def bubble_asc(arr:list) -> list:
    length = len(arr)

    for i in range(length - 1):
        for j in range(0, length -i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def bubble_desc(arr:list) -> list:
    length = len(arr)

    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == "__main__":
    asc = bubble_asc([1, 9, 5, 7, 3, 2])
    print (asc)
    desc = bubble_desc([1, 9, 5, 7, 3, 2])
    print (desc)