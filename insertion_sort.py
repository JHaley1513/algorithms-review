# Insertion sort O(n^2)
arr = []
print("Enter 5 integers:")
for e in range(5):
    arr.append(int(input()))

for j in range(1, 6): # originally started range at 2, since the textbook starts indexing from 1 not 0
    key = arr[j]
    i = j - 1
    while i >= 0 and key < arr[i]: # originally was > 0 according to the book which is > -1 here, but I prefer >= 0 for clarity.
        arr[i + 1] = arr[i]
        i -= 1

for i in range(5):
    print(f'{arr[i]}', end='')
    if i == 4:
        print()
    else:
        print(', ', end='')