
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
int f_gold(int arr[], int n, int sum) {
    int curr_sum, i, j;
    for (i = 0; i < n; i++) {
        curr_sum = arr[i];
        for (j = i + 1; j <= n; j++) {
            if (curr_sum == sum) {
                cout << "Sum found between indexes " << i << " and " << j - 1;
                return 1;
            }
            if (curr_sum > sum || j == n) break;
            curr_sum = curr_sum + arr[j];
        }
    }
    cout << "No subarray found";
    return 0;
}

//TOFILL

template <typename T>
int f_gold(T arr, int n, int sum) {
    if constexpr (is_same_v<T, vector<int>>) {
        return f_gold(&arr.front(), n, sum);
    } else {
        return f_gold(arr, n, sum);
    }
}

// Template wrapper for the undefined function subArraySum
template <typename T>
int subArraySum(T arr, int n, int sum) {
    if constexpr (is_same_v<T, vector<int>>) {
        return subArraySum(&arr.front(), n, sum);
    } else {
        return subArraySum(arr, n, sum);
    }
}

int main() {
    int n_success = 0;
    vector<vector<int>> param0 {{4,8,8,10,15,18,19,22,25,26,30,32,35,36,40,41,43,48,53,57,59,63,64,68,71,76,76,77,78,89,96,97},{-78,16,-16,-10,-2,-38,58,-72,-78,50,-68,-16,-96,82,70,2,-20},{0,0,0,0,0,0,0,0,1,1,1,1,1,1},{16,10,55,43,46,74,57,65,86,60,28,6,92},{-98,-98,-90,-84,-84,-80,-76,-76,-70,-54,-48,-46,-44,-42,-38,-14,-12,-4,6,8,24,28,32,40,40,42,64,84,98},{0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1},{2,10,40,45,56,66,66,70,75,83,93,98},{-20,30,56,-68,54,-6,78,-86,88,-66,76,-66,62,78,22,46,-94,-10,18,16,-36,34,-98,-84,-40,98,82,10,12,54,-88},{0,0,1,1},{38,24,12}};
    vector<int> param1 {26,9,9,10,23,12,10,30,2,1};
    vector<int> param2 {23,12,11,6,19,8,10,17,2,1};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(subArraySum(param0[i], param1[i], param2[i]) == f_gold(param0[i], param1[i], param2[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}
