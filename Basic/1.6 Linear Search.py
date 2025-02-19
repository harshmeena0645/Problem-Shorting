arr = [10, 20, 30, 40, 50]
target = 30

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index", i )
        break
else:
    print("Element not found")