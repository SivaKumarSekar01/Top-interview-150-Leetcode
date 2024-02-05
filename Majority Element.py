from collections import Counter

class Solution:
    def majorityElement(self, nums):
        # Use Counter to count occurrences of each element
        counts = Counter(nums)
        
        # Find the element with the maximum count
        majority_element = max(counts, key=counts.get)
        
        return majority_element

# Example usage:
nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]

sol = Solution()
print(sol.majorityElement(nums1))  # Output: 3
print(sol.majorityElement(nums2))  # Output: 2
