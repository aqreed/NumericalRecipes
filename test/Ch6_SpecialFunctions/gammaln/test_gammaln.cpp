// COMPILATION:
// g++ gammaln.cpp test_gammaln.cpp -o cpptest_gammaln
#include <iostream>
using namespace std;

double gammaln(double x);


int main(int argc, char** argv) {
   /* Function that captures argument, typecasts it to float,
      calculates gammaln and redirects it to stdout */

   double y = stod(argv[1]);
   cout.precision(17);
   cout << gammaln(y) << endl;

   return 0; 
}
