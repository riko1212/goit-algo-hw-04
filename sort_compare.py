import random
import timeit

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Використання вбудованого сортування Timsort
def timsort(arr):
    return sorted(arr)

# Функція для вимірювання часу виконання
def measure_time(sort_func, arr):
    start_time = timeit.default_timer()
    sort_func(arr.copy())
    return timeit.default_timer() - start_time

# Генерація випадкових даних
def generate_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Основна функція для тестування алгоритмів
def main():
    data_sizes = [100, 1000, 5000, 10000]
    sort_functions = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Timsort": timsort
    }

    for size in data_sizes:
        print(f"\nData Size: {size}")
        data = generate_data(size)
        for name, sort_func in sort_functions.items():
            time_taken = measure_time(sort_func, data)
            print(f"{name}: {time_taken:.6f} seconds")

if __name__ == "__main__":
    main()
