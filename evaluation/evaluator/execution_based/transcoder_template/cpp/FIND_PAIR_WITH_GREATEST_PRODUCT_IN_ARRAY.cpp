
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
int f_gold ( int arr [ ], int n ) {
  int result = - 1;
  for ( int i = 0;
  i < n;
  i ++ ) for ( int j = 0;
  j < n - 1;
  j ++ ) for ( int k = j + 1;
  k < n;
  k ++ ) if ( arr [ j ] * arr [ k ] == arr [ i ] ) result = max ( result, arr [ i ] );
  return result;
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
int findGreatest(T arr, int n) {
    if constexpr (is_same_v<T, vector<int>>) {
        return findGreatest(&arr.front(), n);
    } else {
        return findGreatest(arr, n);
    }
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{4,78,84},{-54,64,60,14,18,-68,-54,-58,38,-72,-84,46,74,76,28,-2,54,24,18,-74,-78,14,-38,-70,26,-54,-36,-96,-12,8,62,-42,-84,10,-6,36,-72,10,10,-20,16,92,-64,-34,74,-98,18},{0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{39,49,94,80,48,34,63,82,47,51,60,68,79,23,97,22,54,53,40,2,25},{-90,-52,-10,12,72},{1,0,0},{2,9,11,14,16,17,17,18,19,21,24,25,28,29,30,33,33,39,41,41,43,46,50,51,60,62,67,80,84,86,91,92,97},{4},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1},{52,8,31,92,20,18,34,5,15,8,73,20,40,61,80,51,95,73,38,30,21,69,52,38,68,77}};
    vector<int> param1 {2,26,22,10,3,2,27,0,16,22};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(findGreatest(param0[i],param1[i]) == f_gold(param0[i],param1[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}
