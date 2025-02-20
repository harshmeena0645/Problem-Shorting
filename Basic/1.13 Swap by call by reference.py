def swap_by_reference(data, index1, index2):
    data[index1], data[index2] = data[index2], data[index1]

nums = [5, 10]
print("Before swap:", nums)

# Call the swap function
swap_by_reference(nums, 0, 1)

print("After swap:", nums)