"""Program to find common items from two lists"""
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [4, 5, 7, 8, 9]
print(f'Common items:{[num for num in nums1 if num in nums2]}')  # using list comprehension for common elements
