"""Program to get the difference between the two lists"""
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [4, 5, 7, 8, 9]
print(f'Difference between lists(nums1 - nums2): {[num for num in nums1 if num not in nums2]}')
# accepting only items not in other list
