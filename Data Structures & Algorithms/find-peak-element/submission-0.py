import numpy as np

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return int(np.argmax(nums))
        