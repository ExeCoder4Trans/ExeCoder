
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
int f_gold ( int a, int b, bool x ) {
  int arr [ ] = {
    a, b };
    return ( arr [ x ] );
  }

//TOFILL


int main() {
    int n_success = 0;
    vector<int> param0 {21,17,35,23,48,9,18,46,99,61};
    vector<int> param1 {7,49,43,51,30,44,30,91,23,54};
    vector<int> param2 {34,69,18,80,99,64,34,71,35,5};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(assignValue(param0[i],param1[i],param2[i]) == f_gold(param0[i],param1[i],param2[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}
