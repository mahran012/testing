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
