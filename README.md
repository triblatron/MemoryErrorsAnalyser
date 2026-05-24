# MemoryErrorsAnalyser
A python script to analyse memory errors in GTest executables using valgrind

The idea is to avoid choking valgrind on all the tests.
So they are split into all the individual tests, plus the first test of every parameterised suite.
In the latter case, the theory is that set up and tear down will be equivalent for any of the parameter tuples.
