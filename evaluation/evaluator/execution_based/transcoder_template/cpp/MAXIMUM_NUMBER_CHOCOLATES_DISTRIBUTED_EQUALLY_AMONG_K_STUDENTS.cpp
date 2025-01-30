
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
int f_gold ( int arr [ ], int n, int k ) {
  unordered_map < int, int > um;
  int sum [ n ], curr_rem;
  int maxSum = 0;
  sum [ 0 ] = arr [ 0 ];
  for ( int i = 1;
  i < n;
  i ++ ) sum [ i ] = sum [ i - 1 ] + arr [ i ];
  for ( int i = 0;
  i < n;
  i ++ ) {
    curr_rem = sum [ i ] % k;
    if ( curr_rem == 0 ) {
      if ( maxSum < sum [ i ] ) maxSum = sum [ i ];
    }
    else if ( um . find ( curr_rem ) == um . end ( ) ) um [ curr_rem ] = i;
    else if ( maxSum < ( sum [ i ] - sum [ um [ curr_rem ] ] ) ) maxSum = sum [ i ] - sum [ um [ curr_rem ] ];
  }
  return ( maxSum / k );
}

//TOFILL

template <typename T>
int f_gold(T arr, int n, int k) {
    if constexpr (is_same_v<T, vector<int>>) {
        return f_gold(&arr.front(), n, k);
    } else {
        return f_gold(arr, n, k);
    }
}

template <typename T>
int maxNumOfChocolates(T arr, int n, int k) {
    if constexpr (is_same_v<T, vector<int>>) {
        return maxNumOfChocolates(&arr.front(), n, k);
    } else {
        return maxNumOfChocolates(arr, n, k);
    }
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{2,3,8,8,12,14,23,25,25,27,27,29,40,42,49,52,52,54,56,57,61,68,74,77,81,82,83,84,85,85,85,87,87,88,88,90,92,96,96},{-90,-34,26,-20,-12,-42,28,12,-6,58,-46,4,-30,-28,-14},{0,0,0,0,1,1,1,1,1,1,1,1,1,1,1},{58,81,36,2,51,71,77,34,91,82,47,4,91,83,26,96,3,6},{-92,-86,-82,-68,-60,-46,-40,-28,-26,-24,-2,-2,2,2,10,10,10,16,16,18,20,20,22,30,34,38,56,56,60,62,62,68,82,94,94,98},{0,1,0},{3,8,15,19,21,26,28,31,31,42,45,48,57,75,75,78,79,85,91,99},{-38,42,40,-60,-16,-36,44,60,-86,-38,30,-22,-30,-96,-66},{0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1},{95,38,91,75,43,95,23,36,51,4,38,53,52,58,55,3,19,22,84,9}};
    vector<int> param1 {27,8,7,16,20,2,17,12,13,14};
    vector<int> param2 {32,14,9,12,31,2,16,10,16,19};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(maxNumOfChocolates(param0[i],param1[i],param2[i]) == f_gold(param0[i],param1[i],param2[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}
