
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
bool f_gold ( char str [ ], int k ) {
  int n = strlen ( str );
  int c = 0;
  for ( int i = 0;
  i < k;
  i ++ ) if ( str [ n - i - 1 ] == '0' ) c ++;
  return ( c == k );
}

//TOFILL

template <typename T>
bool f_gold(T arr, int n) {
    if constexpr (is_same_v<T, string>) {
        return f_gold(&arr.front(), n);
    } else {
        return f_gold(arr, n);
    }
}

template <typename T>
bool isDivisible(T arr, int n) {
    if constexpr (is_same_v<T, string>) {
        return isDivisible(&arr.front(), n);
    } else {
        return isDivisible(arr, n);
    }
}

int main() {
    int n_success = 0;
    vector<string> param0 {"111010100","111010100","111010100","111010000","111010000","10110001","tPPdXrYQSI","58211787","011","IkSMGqgzOrteVO"};
    vector<int> param1 {2,2,4,3,4,1,61,73,88,23};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(isDivisible(param0[i],param1[i]) == f_gold(param0[i],param1[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}
