class Solution(object):
    def removeDuplicates(self, nums):
        i = len(nums) - 1
        while i > 0:
            if nums[i] == nums[i-1]:
                nums.pop(i)
            i -= 1

# Example usage
nums = [1, 1, 2, 2, 3, 4, 4, 4, 5]
solution = Solution()
solution.removeDuplicates(nums)
print(nums)  # Modified nums list: [1, 2, 3, 4, 5]
