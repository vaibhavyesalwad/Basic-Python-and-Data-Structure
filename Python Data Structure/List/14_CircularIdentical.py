"""Program to check whether two lists are circularly identical"""


def circular_identical(list1, list2):
    """Functions checks whether given lists are circularly identical and
    returns boolean value for it"""
    if len(list1) != len(list2):
        return False
    list2 = list2 + list2
    return any(list1 == list2[n: n + len(list1)] for n in range(len(list1)))
    # checking combinations n combinations if n elements


nums1 = [1, 2, 3, 2, 6, 1, 1, 4, 5]
nums2 = [1, 4, 5, 1, 2, 3, 2, 6, 1]
print(f'Are nums1 and nums2 circularly identical: {circular_identical(nums1, nums2)}')
