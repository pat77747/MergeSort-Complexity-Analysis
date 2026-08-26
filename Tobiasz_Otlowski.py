import time
import random
import matplotlib.pyplot as plt

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

def measure_time():
    sizes = [1000 * i for i in range(1, 11)]
    times = []

    for size in sizes:
        test_data = [random.randint(0, 100000) for _ in range(size)]
        start = time.time()
        merge_sort(test_data)
        end = time.time()
        times.append(end - start)

    plt.plot(sizes, times, marker='o')
    plt.title('Merge Sort - Czas działania vs. rozmiar danych')
    plt.xlabel('Rozmiar danych')
    plt.ylabel('Czas [s]')
    plt.grid(True)
    plt.savefig("wykres_merge_sort.png")
    plt.show()

if __name__ == "__main__":
    measure_time()
