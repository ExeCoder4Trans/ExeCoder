
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
int f_gold ( int n ) {
  int * dp = new int [ n + 1 ];
  dp [ 0 ] = 0;
  dp [ 1 ] = 1;
  dp [ 2 ] = 2;
  dp [ 3 ] = 3;
  for ( int i = 4;
  i <= n;
  i ++ ) {
    dp [ i ] = i;
    for ( int x = 1;
    x <= ceil ( sqrt ( i ) );
    x ++ ) {
      int temp = x * x;
      if ( temp > i ) break;
      else dp [ i ] = min ( dp [ i ], 1 + dp [ i - temp ] );
    }
  }
  int res = dp [ n ];
  delete [ ] dp;
  return res;
}

//TOFILL

template <typename T>
int f_gold(T arr, int n) {
    if constexpr (is_same_v<T, vector<int>>) {
        return f_gold(n, &arr.front());
    } else {
        return f_gold(n, arr);
    }
}

template <typename T>
int getMinSquares(T n) {
    if constexpr (is_same_v<T, vector<int>>) {
        return getMinSquares(n.front());
    } else {
        return getMinSquares(n);
    }
}

int main() {
    int n_success = 0;
    vector<int> param0 {16,33,47,98,36,81,55,19,4,22};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(getMinSquares(param0[i]) == f_gold(param0[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}
