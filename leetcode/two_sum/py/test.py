import two_sum
import unittest

class TestSolution(unittest.TestCase):
    def testFirstGetSum(self):
        solution = two_sum.Solution()
        getSum = solution.getSum([2, 7, 14, 15], 9)
        self.assertEqual(getSum, [0, 1])
    
    def testSecondGetSum(self):
        solution = two_sum.Solution()
        getSum = solution.getSum([3, 6, 2], 5)
        self.assertEqual(getSum, [0, 2])
    
    def testThirdSolution(self):
        solution = two_sum.Solution()
        getThirdSum = solution.getSum([1, 3, 6, 9], 10)
        self.assertEqual(getThirdSum, [0, 3])

    def testFirstDictSum(self):
        solution = two_sum.Solution()
        getFirstSum = solution.getSumSecond([1, 3, 6, 9], 10)
        self.assertEqual(getFirstSum, [0, 3])

    def testSecondDictSum(self):
        solution = two_sum.Solution()
        getSum = solution.getSumSecond([2, 7, 14, 15], 9)
        self.assertEqual(getSum, [0, 1])
    
    def testThirdDictSum(self):
        solution = two_sum.Solution()
        getSum = solution.getSumSecond([3, 6, 2], 5)
        self.assertEqual(getSum, [0, 2])

    def testFirstOfDictSum(self):
        solution = two_sum.Solution()
        getFirstSum = solution.getSumThird([1, 3, 6, 9], 10)
        self.assertEqual(getFirstSum, [0, 3])

    def testSecondOfDictSum(self):
        solution = two_sum.Solution()
        getSum = solution.getSumThird([2, 7, 14, 15], 9)
        self.assertEqual(getSum, [0, 1])
    
    def testThirdOfDictSum(self):
        solution = two_sum.Solution()
        getSum = solution.getSumThird([3, 6, 2], 5)
        self.assertEqual(getSum, [0, 2])
    

if __name__ == "__main__":
    unittest.main()