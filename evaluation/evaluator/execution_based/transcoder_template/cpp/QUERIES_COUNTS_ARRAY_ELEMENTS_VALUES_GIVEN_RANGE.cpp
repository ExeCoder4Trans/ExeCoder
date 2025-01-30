
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
int f_gold ( int arr [ ], int n, int x, int y ) {
  int count = 0;
  for ( int i = 0;
  i < n;
  i ++ ) {
    if ( arr [ i ] >= x && arr [ i ] <= y ) count ++;
  }
  return count;
}

//TOFILL

// Template wrapper function for f_gold
template <typename T>
int f_gold(T arr, int n, int x, int y) {
    if constexpr (is_same_v<T, vector<int>>) {
        return f_gold(&arr.front(), n, x, y);
    } else {
        return f_gold(arr, n, x, y);
    }
}

// Template wrapper function for countInRange (undefined function)
template <typename T>
int countInRange(T arr, int n, int x, int y) {
    if constexpr (is_same_v<T, vector<int>>) {
        return countInRange(&arr.front(), n, x, y);
    } else {
        return countInRange(arr, n, x, y);
    }
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{9,16,19,24,36,38,42,49,51,53,53,57,57,58,71,78,78,92,92,93},{28,-74,-18,10,26,28,-96,-80,82,94,22,50,72,-90,76,50,20,-44,-80},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{25,8,66,90,50,65,76,90,27},{-98,-96,-90,-82,-80,-78,-70,-66,-60,-60,-50,-48,-34,-26,-24,-16,-14,-8,-6,4,22,24,26,30,30,48,52,56,60,62,74,76,78,86},{1,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0,0,0},{4,6,17,19,24,29,30,31,32,37,37,40,43,44,44,45,57,64,69,70,73,78,86,89,91,92,94},{32,-88,70,-6,28,-48},{0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1},{37,84,97,74,12,26,47,10,14,33}};
    vector<int> param1 {13,18,30,4,32,15,17,4,13,5};
    vector<int> param2 {12,13,21,8,24,16,21,3,12,9};
    vector<int> param3 {13,13,31,5,24,12,15,4,11,8};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(countInRange(param0[i], param1[i], param2[i], param3[i]) == f_gold(param0[i], param1[i], param2[i], param3[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}
