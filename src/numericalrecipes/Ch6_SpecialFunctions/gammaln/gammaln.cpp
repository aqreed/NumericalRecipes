/* Contains the following functions: gammaln */
#include <math.h>
#include <ch6.h>


double gammaln(double xx){
   /* Returns the value of ln[gamma(XX)] for X > 0. Full accuracy
      is obtained for XX > 1.*/

   double stp = 2.50662827465, cof[] = {76.18009173e0, -86.50532033e0,
                                        24.01409822e0, -1.231739516e0,
                                        0.120858003e-2, -0.536382e-5};

   double x = xx - 1.0;
   double tmp = x + 5.5;
   tmp = (x + 0.5) * log(tmp) - tmp;
   double ser = 1.0;

   for(int i=0; i<6; i++){
      x += 1.0;
      ser += cof[i] / x;
   }

   return tmp + log(stp * ser);
}
