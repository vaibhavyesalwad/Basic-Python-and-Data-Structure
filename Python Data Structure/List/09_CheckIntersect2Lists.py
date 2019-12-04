"""Build function that takes two lists and returns True if they have at least one common member"""


def check_common(list1, list2):
    """Function returns True if two given lists have common element(s) else returns False"""
    for item in list1:
        if item in list2:
            return True
    return False


nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 1]
print(f'Do lists have common element(s)? {check_common(nums1, nums2)}')
