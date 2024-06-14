import unittest

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def simple_rob(nums):
            rob, not_rob = 0, 0
            for num in nums:
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.rob([]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.rob([1]), 1)
        self.assertEqual(self.solution.rob([10]), 10)

    def test_two_elements(self):
        self.assertEqual(self.solution.rob([1, 2]), 2)
        self.assertEqual(self.solution.rob([2, 1]), 2)

    def test_multiple_elements(self):
        self.assertEqual(self.solution.rob([2, 3, 2]), 3)
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 11)
        self.assertEqual(self.solution.rob([5, 5, 10, 100, 10, 5]), 110)

    def test_complex_case(self):
        self.assertEqual(self.solution.rob([6, 7, 1, 30, 8, 2, 4]), 41)
        self.assertEqual(self.solution.rob([1, 3, 1, 3, 100]), 103)

if __name__ == '__main__':
    unittest.main()


