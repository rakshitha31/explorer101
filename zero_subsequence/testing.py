import zero_subsequence
import unittest
import random

class Test_Zero_Sequence(unittest.TestCase):
    def test_all_zeros(self):
        matrix=[[0 for i in range(10)]for j in range(10)]
        result=zero_subsequence.count_squence(10, matrix)
        self.assertDictEqual(result, {3:0,4:0,5:0, 6:0, 7:0,8:0, 9:0, 10:10})

    def test_all_ones(self):
        matrix=[[1 for i in range(10)]for j in range(10)]
        result=zero_subsequence.count_squence(10, matrix)
        self.assertDictEqual(result, {3:0,4:0,5:0, 6:0, 7:0,8:0, 9:0, 10:0})

    def test_non_binary(self):
        matrix=[[random.randint(1,10) for i in range(10)]for j in range(10)]
        result=zero_subsequence.count_squence(10,matrix)
        self.assertDictEqual(result, {3:0,4:0,5:0, 6:0, 7:0,8:0, 9:0, 10:0})

    
if __name__ == '__main__':
    unittest.main()