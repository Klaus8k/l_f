from typing import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = b = 0
        ref = [nums[0],]
        
        for i in range(len(nums)):
            if nums[a] in ref:
                nums[a] = nums[a]+1
            else:
                
                ref.append(nums[i])
                a += 1
        print(nums)

        return b

        # set_nums = set(nums)
        # len_nums = len(nums)
        # nums = sorted(list(set_nums))

        # add_list = ['_' for i in range(len_nums - len(set_nums))]
        # return len(nums), nums + add_list


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(nums))
