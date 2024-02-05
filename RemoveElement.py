class Solution(object):
    def removeElement(self, nums, val):
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == val:
                nums.pop(i)
            i -= 1

        return len(nums)

# Example usage
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
result = solution.removeElement(nums, val)
print(result)  # Output: 2
print(nums)    # Modified nums list: [2, 2]
