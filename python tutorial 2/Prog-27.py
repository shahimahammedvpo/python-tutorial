def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

nums = list(map(int, input("Enter numbers: ").split()))
bubble_sort(nums)
print("Sorted list:", nums)
