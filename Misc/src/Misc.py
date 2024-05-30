import unittest


class Test(unittest.TestCase):

    def testChainingComparisons(self):
        i = 5
        j = 10
        k = 15
        self.assertTrue(i < j < k)
        self.assertFalse(i < k < j)

    def testJoinMethod(self):
        question = 'Life, the Universe, and Everything'
        answer = 42
        text = " ".join([str(answer),
                         "is the Answer to the Ultimate Question of",
                         question])
        self.assertEqual(text,
                         "42 is the Answer to the Ultimate Question of Life, the Universe, and Everything")

    def testPercentageOperator(self):
        question = 'Life, the Universe, and Everything'
        answer = 42
        text = "%s is the Answer to the Ultimate Question of %s" % (answer, question)
        self.assertEqual(text,
                         "42 is the Answer to the Ultimate Question of Life, the Universe, and Everything")

    def testFormatMethod(self):
        question = 'Life, the Universe, and Everything'
        answer = 42
        text = "{in2} is the Answer to the Ultimate Question of {in1}".format(in1=question, in2=answer)
        self.assertEqual(text,
                         "42 is the Answer to the Ultimate Question of Life, the Universe, and Everything")

    def testFStrings(self):
        question = 'Life, the Universe, and Everything'
        answer = 42
        self.assertEqual(f'{answer} is the Answer to the Ultimate Question of {question}',
                         "42 is the Answer to the Ultimate Question of Life, the Universe, and Everything")

    def testForLoopElse(self):
        for x in range(6):
            if x == 7: break
            pass
        else:
            self.assertTrue(True)

        for x in range(6):
            if x == 3: break
            pass
        else:
            self.assertTrue(False)

    def testImaginaryNumbers(self):
        v1 = 5 + 2j
        v2 = 10 + 3j
        v = v1 + v2
        self.assertEqual(v, 15 + 5j)
        self.assertEqual(v.real, 15)
        self.assertEqual(v.imag, 5)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
