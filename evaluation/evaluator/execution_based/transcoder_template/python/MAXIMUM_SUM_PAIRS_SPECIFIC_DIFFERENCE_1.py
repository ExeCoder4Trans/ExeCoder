# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , N , k ) :
    maxSum = 0 ;
    arr.sort ( ) ;
    i = N - 1 ;
    while ( i >= 0 ) :
        if ( arr [ i ] - arr [ i - 1 ] < k ) :
            maxSum += arr [ i ] ;
            maxSum += arr [ i - 1 ] ;
            i -= 1 ;
        i -= 1 ;
    return maxSum ;


#TOFILL

if __name__ == '__main__':
    param = [
    ([2, 10, 11, 11, 12, 14, 15, 17, 27, 27, 28, 36, 36, 44, 47, 47, 54, 55, 62, 64, 68, 69, 70, 70, 75, 76, 78, 85, 85, 91, 95, 97],26,18,),
    ([-36, 78, 10, 30, -12, -70, -98, -14, -44, -66, -40, -8, 78, 2, -70, 40, 92, 58, 30, 10, -84, -62, -86, -50, 82, 36, -92, -30, -2, -34, 88, 2, -4, -72],26,25,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],47,26,),
    ([77, 78, 58],1,1,),
    ([-88, -88, -88, -82, -58, -54, -48, -46, -46, -44, -20, -2, 10, 28, 28, 28, 42, 42, 44, 50, 50, 54, 56, 58, 62, 68, 70, 72, 74, 76, 78, 88, 90, 92],21,24,),
    ([0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],41,40,),
    ([5, 7, 10, 11, 15, 17, 20, 20, 29, 29, 32, 37, 38, 39, 40, 41, 45, 51, 60, 64, 64, 68, 68, 70, 71, 71, 71, 75, 76, 82, 84, 87, 88, 88, 95, 98],30,21,),
    ([-46, -32, 76, -28, 44, -14, 94, -4, 60, -88, -52, 32, -66, 28, 94, 76, 86, -4, 74, 52, 64, -36, -98, -40, 70, 18, -22, -20, -16, -74, 12, 60, 94, 98, -28, -24, 4, -34, -60, 56],33,23,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],28,41,),
    ([79, 13, 25, 22, 61, 1, 2, 73, 66, 94, 47, 9, 1, 99, 25, 39, 95, 46, 95, 20, 63, 15, 14, 36, 9, 91, 14],19,23,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if maxSumPairWithDifferenceLessThanK(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))