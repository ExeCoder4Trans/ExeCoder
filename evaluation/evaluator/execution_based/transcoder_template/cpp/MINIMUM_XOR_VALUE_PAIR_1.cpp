
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
int f_gold ( int arr [ ], int n ) {
  sort ( arr, arr + n );
  int minXor = INT_MAX;
  int val = 0;
  for ( int i = 0;
  i < n - 1;
  i ++ ) {
    val = arr [ i ] ^ arr [ i + 1 ];
    minXor = min ( minXor, val );
  }
  return minXor;
}

//TOFILL

template <typename T>
int f_gold(T arr, int n) {
    if constexpr (is_same_v<T, vector<int>>) {
        return f_gold(&arr.front(), n);
    } else {
        return f_gold(arr, n);
    }
}

template <typename T>
int minXOR(T arr, int n) {
    if constexpr (is_same_v<T, vector<int>>) {
        return minXOR(&arr.front(), n);
    } else {
        return minXOR(arr, n);
    }
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{8,11,12,27,32,32,36,56,57,66,68,70,74,78,82,83,96},{40,48,66,4,-60,42,-8,38},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{98,6,82,95,87,20,11,63,78,70,37,12,57,67,10,49,38,28,86,7,61,50,32,68,91,66,57,29,2,64,65,15,16,4,7,76,44,52,81,89,3,36,57,95,48,24},{-88,-84,-76,-58,-40,-38,-28,-24,-20,-14,-12,16,20,28,28,30,40,44,56,58,60,92,92},{0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,0,1,0},{6,6,19,31,41,45,49,56,78,96,98},{62,-90,22,-84,-4},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1},{83,13,43,99,34,74,56,20,93,65,92,58,91,72,37,10,39,7,29,69,42,28}};
    vector<int> param1 {10,7,19,36,13,20,6,3,21,14};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(minXOR(param0[i],param1[i]) == f_gold(param0[i],param1[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}
