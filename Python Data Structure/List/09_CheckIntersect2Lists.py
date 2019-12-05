"""Build function that takes two lists and returns True if they have at least one common member"""


def check_common(list1, list2):
    """Function returns True if two given lists have common element(s) else returns False"""
    return any(num in list2 for num in list1)


nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 3]
print(f'Do lists have common element(s)? {check_common(nums1, nums2)}')
