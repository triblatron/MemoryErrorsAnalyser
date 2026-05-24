import unittest
from parameterized import *
from MemoryErrorsAnalyser import *

class MemoryErrorAnalyserTest(unittest.TestCase):
    @parameterized.expand([
        ("./bin/DagBaseTest", "data/tests/MemoryErrorsAnalyser/OneTest.txt", 1, 0, "Coroutine.testReturnsNullWhenNotGivenAFunction", "--log-file=Coroutine_testReturnsNullWhenNotGivenAFunction.txt --leak-check=full --track-origins=yes ./bin/DagBaseTest --gtest_filter=Coroutine.testReturnsNullWhenNotGivenAFunction"),
        ("./bin/DagBaseTest", "data/tests/MemoryErrorsAnalyser/TwoTests.txt", 2, 1, "Coroutine.testReturnsACoroutineIfGivenAFunction", "--log-file=Coroutine_testReturnsACoroutineIfGivenAFunction.txt --leak-check=full --track-origins=yes ./bin/DagBaseTest --gtest_filter=Coroutine.testReturnsACoroutineIfGivenAFunction"),
        ("./bin/DagBaseTest", "data/tests/MemoryErrorsAnalyser/ParameterisedTests.txt", 1, 0, "ConfigurationElement/ConfigurationElement_testFindElement.testFindFromRoot/0", "--log-file=ConfigurationElement_ConfigurationElement_testFindElement_testFindFromRoot_0.txt --leak-check=full --track-origins=yes ./bin/DagBaseTest --gtest_filter=ConfigurationElement/ConfigurationElement_testFindElement.testFindFromRoot/0")
    ])
    def test_ctor(self, exe, test_filename, num_tests, test_index, test_name, args):
        sut = MemoryErrorsAnalyser(exe, test_filename)
        self.assertEqual(num_tests, len(sut.tests))
        self.assertEqual(test_name, sut.tests[test_index])
        self.assertEqual(args, sut.commands[test_index])

if __name__ == '__main__':
    unittest.main()
