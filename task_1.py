import random
import timeit

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Generate datasets
def generate_data(size, data_type='random'):
    if data_type == 'random':
        return [random.randint(0, size) for _ in range(size)]
    elif data_type == 'sorted':
        return list(range(size))
    elif data_type == 'reversed':
        return list(range(size, 0, -1))

# Test sorting algorithms
def test_sorting_algorithms():
    sizes = [100, 1000, 10000]
    data_types = ['random', 'sorted', 'reversed']

    print(f"{'Size':<10}{'Type':<10}{'Algorithm':<15}{'Time (s)':<10}")
    print("-" * 45)

    for size in sizes:
        for data_type in data_types:
            data = generate_data(size, data_type)

            # Measure Merge Sort
            merge_time = timeit.timeit(lambda: merge_sort(data), number=1)
            print(f"{size:<10}{data_type:<10}{'Merge Sort':<15}{merge_time:<10.6f}")

            # Measure Insertion Sort (only for small sizes, as it is slow)
            if size <= 1000:
                insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
                print(f"{size:<10}{data_type:<10}{'Insertion Sort':<15}{insertion_time:<10.6f}")

            # Measure Timsort (Python's built-in sorted)
            timsort_time = timeit.timeit(lambda: sorted(data), number=1)
            print(f"{size:<10}{data_type:<10}{'Timsort':<15}{timsort_time:<10.6f}")

# Run the tests
if __name__ == "__main__":
    test_sorting_algorithms()
