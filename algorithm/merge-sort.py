def merge_sort(arr: list, bottom: int, top: int) -> None:
    if top <= bottom:
        return
    
    mid = (bottom + top) // 2
    merge_sort(arr, bottom, mid)
    merge_sort(arr, mid + 1, top)

    merge(arr, bottom, mid, top)

def merge(arr: list, bottom: int, mid: int, top: int) -> None:
    left = arr[bottom:mid + 1]  # Slice notation to get left sublist
    right = arr[mid + 1:top + 1]  # Slice notation to get right sublist

    i = j = 0
    k = bottom  # Index for merging back into the original list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

if __name__ == "__main__":
    arr = [1, 9, 5, 7, 3, 2, 8]
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted Array:", arr)
