# Bubble Sort in Python

def bubble_sort(nums):
    n = len(nums)
    
    # Traverse through all elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):

            # Swap if the element found is greater than the next element
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

# ---- Input + Output ----
# User enters numbers separated by spaces
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Sorting the numbers
sorted_numbers = bubble_sort(numbers)

print("Sorted list:", sorted_numbers)
