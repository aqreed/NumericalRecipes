# !/bin/bash
# calls the code coverage testing program gcov

# clean, link and compile the cpp files
make clean
make 

# run tests, with test coverage (see makefile flags)
./test/Ch6_SpecialFunctions/gammaln/cpptest_gammaln

# gcc suite test coverage
gcov test/Ch6_SpecialFunctions/gammaln/gammaln.cpp

# code coverage is in the files "*.cpp.gcov"
