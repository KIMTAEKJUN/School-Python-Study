# 선택정렬
arr = [ 7, 5, 9, 0, 3, 1, 6, 2, 4, 8 ]

for i in range(len(arr)):
    A = i
    for j in range(i + 1, len(arr)):
        if arr[A] > arr[j]:
            A=j
    arr[i], arr[A] = arr[A], arr[i]
print(arr)