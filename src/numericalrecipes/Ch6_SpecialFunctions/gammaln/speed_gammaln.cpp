// COMPILATION:
// g++ gammaln.cpp speed_gammaln.cpp -o cppSpeed_gammaln
#include <iostream>
#include <chrono>
using namespace std;

double gammaln(float x);


int main() {
   /* Function that measures elapsed time of a for loop
      that calculates gammaln */

   // Input data
   float gl, x = 0.25;

   // Timing of the for loop
   auto start = chrono::steady_clock::now();

   for(int i=0; i<1e6; i++){
      gl = gammaln(x);
   }

   auto end = chrono::steady_clock::now();

   cout << gl << " " << chrono::duration_cast<chrono::milliseconds>(end - start).count()
      << endl;
   return 0;
}
