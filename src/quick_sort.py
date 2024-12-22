import pandas as pd
import time
import matplotlib.pyplot as plt

# Memuat Dataset restaurant
file_path = 'restaurant_data.csv'
restaurant_data = pd.read_csv(file_path)

# Fungsi QuickSort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Test algoritma quick sort dengan ukuran berbeda
sizes = [10, 200, 1000, 3000, 7000]
runtimes = []

if 'Revenue' in restaurant_data.columns:
    for size in sizes:
        if size <= len(restaurant_data):
            test_data = restaurant_data['Revenue'][:size].tolist()
            start_time = time.time()
            quick_sort(test_data)
            elapsed_time = time.time() - start_time
            runtimes.append(elapsed_time)
            print(f"Size: {size}, Time taken: {elapsed_time:.6f} seconds")
        else:
            print(f"Size: {size} exceeds the dataset size.")
else:
    print("The column 'Revenue' does not exist in the dataset.")

# Menampilkan dalam graf
plt.figure(figsize=(10, 6))
plt.plot(sizes, runtimes, marker='o', linestyle='-', color='b', label='Quick Sort Runtime')
plt.title('Quick Sort Runtime vs. Data Size', fontsize=14)
plt.xlabel('Data Size', fontsize=12)
plt.ylabel('Runtime (seconds)', fontsize=12)
plt.ylim(0, 5)  # Mengatur batasan sumbu y
plt.grid(True)
plt.legend()
plt.show()
