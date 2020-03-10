# Test coverage is achieved using gcov (part of gcc suite),
# with the flags -ftest-coverage and -fprofile-arcs
LIBDIR = src/numericalrecipes/Ch6_SpecialFunctions
TESTDIR = test/Ch6_SpecialFunctions/gammaln

CXX = g++
CXXFLAGS = -I $(LIBDIR) -Wall -ftest-coverage -fprofile-arcs

LIB = $(patsubst %, $(LIBDIR)/%, gammaln/gammaln.cpp)
TEST = $(patsubst %, $(TESTDIR)/%, test_gammaln.cpp)
OBJ = $(patsubst %, $(TESTDIR)/%, test_gammaln.o gammaln.o)

$(TESTDIR)/cpptest_gammaln: $(OBJ)
	$(CXX) -o $@ $^ $(CXXFLAGS) -lm -lncurses -Os

$(TESTDIR)/test_gammaln.o: $(TEST)
	$(CXX) -c -o $@ $< $(CXXFLAGS)

$(TESTDIR)/gammaln.o: $(LIB)
	$(CXX) -c -o $@ $< $(CXXFLAGS)

clean:
	cd $(TESTDIR); rm -f *.out *.o *.gc* *.info cpptest_gammaln
