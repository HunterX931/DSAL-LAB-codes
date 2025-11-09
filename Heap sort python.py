def max_heapify(a, i, n):
    temp = a[i]
    j = 2 * i

    while j <= n:
        if j < n and a[j + 1] > a[j]:
            j = j + 1
        if temp > a[j]:
            break
        else:
            a[j // 2] = a[j]
            j = 2 * j

    a[j // 2] = temp


def build_max_heap(a, n):
    for i in range(n // 2, 0, -1):
        max_heapify(a, i, n)


def max_heapsort(a, n):
    for i in range(n, 1, -1):
        a[i], a[1] = a[1], a[i]  # swap
        max_heapify(a, 1, i - 1)


def min_heapify(a, i, n):
    temp = a[i]
    j = 2 * i

    while j <= n:
        if j < n and a[j + 1] < a[j]:
            j = j + 1
        if temp < a[j]:
            break
        else:
            a[j // 2] = a[j]
            j = 2 * j

    a[j // 2] = temp


def build_min_heap(a, n):
    for i in range(n // 2, 0, -1):
        min_heapify(a, i, n)


def min_heapsort(a, n):
    for i in range(n, 1, -1):
        a[i], a[1] = a[1], a[i]  # swap
        min_heapify(a, 1, i - 1)


def print_array(arr, n):
    print("\nSorted Data: ", end="")
    for i in range(1, n + 1):
        print("->", arr[i], end="")
    print()


def main():
    n = int(input("Enter the number of data elements to be sorted: "))
    arr = [0]  # dummy element at index 0 for 1-based indexing

    for i in range(1, n + 1):
        value = int(input(f"Enter element {i}: "))
        arr.append(value)

    while True:
        print("\n1. Heap sort using max heap")
        print("2. Heap sort using min heap")
        print("3. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            build_max_heap(arr, n)
            max_heapsort(arr, n)
            print_array(arr, n)
        elif ch == 2:
            build_min_heap(arr, n)
            min_heapsort(arr, n)
            print_array(arr, n)
        elif ch == 3:
            break
        else:
            print("Invalid choice! Please enter again.")


if __name__ == "__main__":
    main()

