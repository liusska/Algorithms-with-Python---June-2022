def reverse_array(idx, array):
    if idx == len(array) // 2:
        return
    swap_idx = len(array) - 1 - idx
    array[idx], array[swap_idx] = array[swap_idx], array[idx]
    reverse_array(idx+1, array)


elements = input().split()
reverse_array(0, elements)
print(' '.join(elements))
