class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1         # Last inder nums1

        while m > 0 and n > 0:       # merge in reverse order
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        while n > 0:                  # fill nums1 with leftover nums2 element
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1       
            
        