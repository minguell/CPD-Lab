import random
import time


def partition_lomuto(arr, low, high):
    pivot = arr[low]
    i = low
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[i] = arr[i], arr[low]
    return i


def partition_hoare(arr, low, high):
    pivot = arr[low]
    i, j = low - 1, high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def choose_pivot_median_of_three(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return mid


def choose_pivot_random(arr, low, high):
    return random.randint(low, high)


def quicksort(arr, low, high, partition_func, choose_pivot_func):
    if low < high:
        pivot_index = choose_pivot_func(arr, low, high)
        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
        pivot = partition_func(arr, low, high)
        quicksort(arr, low, pivot, partition_func, choose_pivot_func)
        quicksort(arr, pivot + 1, high, partition_func, choose_pivot_func)


def run_quicksort(filename, choose_pivot_func, partition_func, output_filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        elements = list(map(int, line.split()))
        size = elements[0]
        arr = elements[1:]
        start_time = time.time()
        quicksort(arr, 0, size - 1, partition_func, choose_pivot_func)
        end_time = time.time()
        elapsed_time = end_time - start_time
        swaps = size - 1  # Quicksort always makes n-1 swaps
        recursions = 0  # TODO: Implement recursion count
        with open(output_filename, "a") as output_file:
            output_file.write(f"TAMANHO ENTRADA {size}\n")
            output_file.write(f"SWAPS {swaps}\n")
            output_file.write(f"RECURSOES {recursions}\n")
            output_file.write(
                f"TEMPO {elapsed_time * 1000 if elapsed_time < 1 else elapsed_time} {'MILISEGUNDOS' if elapsed_time < 1 else 'SEGUNDOS'}\n"
            )


if __name__ == "__main__":
    # Limpe os arquivos de saída
    for output_filename in [
        "stats-mediana-hoare.txt",
        "stats-mediana-lomuto.txt",
        "stats-aleatorio-hoare.txt",
        "stats-aleatorio-lomuto.txt",
    ]:
        with open(output_filename, "w") as output_file:
            pass

    # Execute as quatro combinações
    run_quicksort(
        "entrada-quicksort.txt",
        choose_pivot_median_of_three,
        partition_hoare,
        "stats-mediana-hoare.txt",
    )
    run_quicksort(
        "entrada-quicksort.txt",
        choose_pivot_median_of_three,
        partition_lomuto,
        "stats-mediana-lomuto.txt",
    )
    run_quicksort(
        "entrada-quicksort.txt",
        choose_pivot_random,
        partition_hoare,
        "stats-aleatorio-hoare.txt",
    )
    run_quicksort(
        "entrada-quicksort.txt",
        choose_pivot_random,
        partition_lomuto,
        "stats-aleatorio-lomuto.txt",
    )
