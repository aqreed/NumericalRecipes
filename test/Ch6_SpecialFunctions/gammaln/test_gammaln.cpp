/* Test file for gammaln function */
#include <stdio.h>
#include <math.h>
#include <ch6.h>

#define S_OK (0)
#define E_FAIL (-1)
#define EPSILON (1e-4)


/* **************************************
    Test cases for the gammaln functions
   **************************************
*/
int test_gammaln(){
    /*
        Checks values x > 0
    */
    double x1 = 0.01, x2 = 1.0, x3 = 2.0, x4 = 5.0, c1, c2, c3, c4;

    c1 = gammaln(x1);
    c2 = gammaln(x2);
    c3 = gammaln(x3);
    c4 = gammaln(x4);

    double calculated_value[] = {c1, c2, c3, c4};
    double expected_value[] = {4.599479878042021722514, 0,
                                0, 3.178053830347945619647};

    for (int i=0; i<=3; i++) {
        if (fabs(calculated_value[i] - expected_value[i]) > EPSILON){
            return E_FAIL;
        }
    }
    return S_OK;
}


int test_gammaln_recurrence(){
    /*
        Gamma function satisfies the recurrence relation:
            gamma(z+1) = z * gamma(z)

        Accordingly, this test checks that gamma log satisfies:
            gammaln(z+1) = ln(z) + gammaln(z)
    */
    double x1 = 0.001, x2 = 1.1, x3 = 3.32, x4 = 23.11, c1, c2, c3, c4;

    c1 = gammaln(x1 + 1) - (log(x1) + gammaln(x1));
    c2 = gammaln(x2 + 1) - (log(x2) + gammaln(x2));
    c3 = gammaln(x3 + 1) - (log(x3) + gammaln(x3));
    c4 = gammaln(x4 + 1) - (log(x4) + gammaln(x4));

    double calculated_value[] = {c1, c2, c3, c4};
    double expected_value[] = {0, 0, 0, 0};

    for (int i=0; i<=3; i++) {
        if (fabs(calculated_value[i] - expected_value[i]) > EPSILON){
            return E_FAIL;
        }
    }
    return S_OK;
}


int factorial(int n){
    return (n==1 || n==0) ? 1: n * factorial(n - 1);
}


int test_gammaln_factorial(){
    /*
        Gamma function satisfies the recurrence relation for
        positive integer values:
            gamma(z) = (z-1)!

        Accordingly, this test checks that gamma log satisfies:
            exp[gammaln(z)] = (z-1)!
    */
    double x1 = 1, x2 = 2, x3 = 6, x4 = 9, c1, c2, c3, c4;

    c1 = exp(gammaln(x1)) - factorial(x1 - 1);
    c2 = exp(gammaln(x2)) - factorial(x2 - 1);
    c3 = exp(gammaln(x3)) - factorial(x3 - 1);
    c4 = exp(gammaln(x4)) - factorial(x4 - 1);

    double calculated_value[] = {c1, c2, c3, c4};
    double expected_value[] = {0, 0, 0, 0};

    for (int i=0; i<=3; i++){
        if (fabs(calculated_value[i] - expected_value[i]) > EPSILON){
            return E_FAIL;
        }
    }
    return S_OK;
}

/* ************
    Test suite
   ************
*/
int run_tests(){
    if (test_gammaln() == E_FAIL){
        printf("Failed test_gammaln()\n");
        return E_FAIL;
    } else if (test_gammaln_recurrence() == E_FAIL){
        printf("Failed test_gammaln_recurrence()\n");
        return E_FAIL;
    } else if (test_gammaln_factorial() == E_FAIL){
        printf("Failed test_gammaln_factorial()\n");
        return E_FAIL;
    } else {
        return S_OK;
    }
}

/* ********************************************************************
    Main function to run the test code. If successful it returns S_OK,
    equal to the numerical value of 0. Any other value is a failure.
   ********************************************************************
*/
int main(){
    int result;

    printf("Running tests...\n");
    result = run_tests();

    if (result == S_OK)
        printf("Tests passed\n");
    else
        printf("Tests failed\n");

    return result;
}
