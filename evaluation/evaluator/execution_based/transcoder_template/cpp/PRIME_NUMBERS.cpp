// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
bool f_gold ( int n ) {
  if ( n <= 1 ) return false;
  for ( int i = 2;
  i < n;
  i ++ ) if ( n % i == 0 ) return false;
  return true;
}


//TOFILL

int main() {
    int n_success = 0;
    vector<int> param0 {2,74,46,38,51,48,6,14,31,10};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(isPrime(param0[i]) == f_gold(param0[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}