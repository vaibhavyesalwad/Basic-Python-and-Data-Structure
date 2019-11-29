"""Sort numbers in list using Merge Sort algorithm"""


def merge_sort(arr):
    if len(arr) > 1:                     # at max divide into sub-array  until size of sub-array is at least 1
        mid = len(arr)//2
        L = arr[:mid]                     # array(super-array) divide into left & right sub-arrays
        R = arr[mid:]
        merge_sort(L)                   # call merge_sort for sub-array
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):            # merging two sub-arrays while comparing & sorting
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):                   # if some elements are yet be compared and added to super-array
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


numbers = [int(i) for i in input('Enter list of numbers:').split()]
print(numbers)
merge_sort(numbers)
print(numbers)