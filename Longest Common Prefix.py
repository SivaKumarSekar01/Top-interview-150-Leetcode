class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        strs.sort()
        first_str = strs[0]
        last_str = strs[-1]

        common_prefix = []
        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            else:
                break

        return ''.join(common_prefix)

# Example usage:
solution_instance = Solution()
strs1 = ["flower", "flow", "flight"]
print(solution_instance.longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(solution_instance.longestCommonPrefix(strs2))  # Output: ""
