# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( mat , n ) :
    diag1_left = 0
    diag1_right = 0
    diag2_left = 0
    diag2_right = 0
    i = 0
    j = n - 1
    while i < n :
        if ( i < n // 2 ) :
            diag1_left += mat [ i ] [ i ]
            diag2_left += mat [ j ] [ i ]
        elif ( i > n // 2 ) :
            diag1_right += mat [ i ] [ i ]
            diag2_right += mat [ j ] [ i ]
        i += 1
        j -= 1
    return ( diag1_left == diag2_right and diag2_right == diag2_left and diag1_right == diag2_left and diag2_right == mat [ n // 2 ] [ n // 2 ] )


#TOFILL

if __name__ == '__main__':
    param = [
        ([[2, 9, 1, 4, -2],
         [6, 7, 2, 11, 4],
         [ 4, 2, 9, 2, 4],
         [1, 9, 2, 4, 4 ],
         [ 0, 2, 4, 2, 5]],5,),
    ([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],8,),
    ([[52, 88, 22, 69, 1, 83, 30, 39, 79, 35, 69, 70, 89, 11, 51, 63, 86, 34, 55, 78, 73, 20, 80, 58, 81, 17, 34, 75, 99, 62, 34, 72, 19, 97, 87, 66, 72, 93, 42, 51, 71, 49, 29, 95], [30, 99, 25, 68, 62, 38, 17, 74, 1, 18, 63, 46, 19, 50, 96, 54, 31, 97, 86, 65, 46, 35, 49, 81, 34, 29, 6, 1, 55, 27, 12, 4, 80, 52, 11, 52, 84, 26, 28, 72, 66, 90, 27, 97], [55, 71, 54, 46, 36, 21, 49, 34, 87, 34, 40, 7, 90, 52, 49, 81, 95, 89, 37, 62, 15, 2, 11, 96, 94, 17, 88, 45, 68, 61, 46, 32, 19, 67, 4, 25, 73, 21, 87, 93, 94, 89, 93, 98], [14, 22, 48, 51, 80, 11, 59, 14, 7, 69, 58, 40, 93, 81, 94, 25, 78, 42, 86, 44, 5, 28, 76, 60, 77, 21, 96, 49, 56, 57, 85, 61, 38, 73, 2, 3, 43, 74, 35, 73, 40, 96, 85, 58], [34, 25, 56, 32, 22, 89, 65, 21, 80, 96, 21, 28, 19, 14, 87, 24, 20, 32, 74, 52, 65, 95, 52, 58, 79, 95, 92, 10, 70, 15, 47, 91, 10, 21, 19, 68, 22, 63, 38, 15, 70, 75, 44, 30], [24, 86, 94, 46, 4, 6, 38, 26, 19, 2, 68, 69, 47, 99, 29, 64, 80, 12, 85, 73, 11, 8, 60, 26, 32, 39, 4, 98, 92, 89, 44, 99, 83, 35, 51, 51, 29, 78, 85, 36, 78, 60, 15, 51], [50, 94, 55, 12, 50, 62, 5, 27, 79, 90, 9, 35, 13, 44, 46, 97, 98, 68, 77, 74, 53, 1, 11, 50, 9, 38, 87, 13, 5, 25, 10, 5, 22, 42, 89, 20, 28, 21, 11, 93, 69, 37, 49, 69], [33, 45, 8, 6, 15, 15, 9, 61, 56, 5, 26, 87, 80, 57, 35, 10, 91, 80, 21, 12, 9, 16, 73, 93, 54, 23, 39, 88, 22, 55, 31, 74, 47, 27, 98, 48, 39, 88, 21, 15, 81, 45, 19, 53], [89, 55, 86, 49, 78, 61, 60, 92, 76, 91, 24, 86, 39, 61, 23, 72, 92, 93, 79, 39, 72, 92, 97, 11, 42, 25, 34, 22, 2, 51, 16, 11, 78, 96, 86, 69, 87, 62, 19, 29, 42, 23, 60, 73], [18, 95, 81, 55, 18, 27, 85, 1, 96, 14, 59, 78, 33, 36, 39, 76, 45, 25, 15, 20, 34, 58, 60, 78, 30, 13, 78, 93, 90, 67, 89, 91, 45, 40, 80, 38, 75, 93, 47, 88, 29, 34, 11, 20], [20, 73, 56, 23, 91, 88, 25, 89, 33, 31, 74, 79, 1, 54, 16, 85, 59, 66, 3, 15, 32, 50, 91, 99, 60, 88, 8, 7, 4, 94, 10, 60, 25, 42, 47, 96, 96, 32, 74, 73, 25, 89, 16, 49], [16, 94, 38, 5, 7, 77, 8, 33, 62, 74, 84, 32, 93, 1, 91, 20, 55, 63, 78, 79, 6, 52, 2, 93, 39, 32, 51, 69, 86, 92, 32, 93, 3, 62, 95, 13, 70, 21, 61, 14, 89, 71, 22, 32], [41, 32, 42, 52, 94, 81, 54, 62, 85, 90, 43, 3, 38, 81, 39, 70, 85, 45, 46, 13, 52, 9, 57, 69, 43, 7, 44, 44, 95, 68, 77, 44, 79, 40, 77, 43, 62, 43, 90, 19, 49, 65, 77, 25], [84, 41, 23, 58, 88, 43, 40, 30, 34, 10, 60, 1, 12, 46, 93, 75, 17, 84, 58, 38, 6, 62, 84, 74, 10, 95, 26, 58, 17, 53, 78, 5, 67, 20, 51, 46, 79, 67, 3, 23, 9, 11, 47, 49], [44, 13, 8, 63, 22, 38, 27, 26, 23, 95, 93, 65, 74, 47, 61, 46, 4, 31, 4, 29, 73, 79, 44, 3, 59, 79, 53, 11, 6, 47, 7, 68, 85, 1, 56, 87, 77, 43, 28, 29, 18, 87, 92, 73], [62, 6, 16, 1, 22, 46, 62, 23, 21, 51, 95, 38, 28, 44, 91, 39, 42, 42, 60, 57, 77, 96, 7, 51, 97, 77, 32, 7, 76, 40, 15, 59, 85, 12, 77, 42, 39, 63, 2, 29, 61, 29, 38, 7], [30, 87, 92, 56, 87, 36, 42, 93, 4, 84, 5, 46, 75, 2, 54, 88, 59, 33, 22, 47, 6, 24, 93, 49, 96, 94, 51, 41, 67, 89, 92, 79, 81, 2, 91, 78, 43, 32, 12, 23, 16, 44, 2, 7], [21, 58, 95, 23, 60, 25, 35, 99, 45, 7, 69, 32, 53, 69, 25, 95, 84, 86, 77, 2, 86, 61, 9, 51, 2, 45, 32, 72, 80, 97, 75, 32, 8, 96, 85, 89, 20, 65, 21, 7, 89, 9, 86, 2], [19, 60, 70, 59, 69, 45, 62, 10, 65, 26, 90, 60, 18, 59, 21, 46, 12, 78, 32, 39, 99, 81, 55, 55, 10, 35, 80, 6, 68, 62, 9, 29, 71, 80, 6, 44, 64, 67, 44, 78, 14, 9, 23, 57], [57, 15, 64, 7, 20, 64, 19, 6, 51, 39, 65, 71, 99, 25, 23, 89, 58, 11, 34, 31, 38, 46, 12, 9, 13, 64, 20, 59, 85, 22, 65, 60, 41, 81, 45, 4, 70, 45, 58, 83, 94, 23, 32, 63], [93, 8, 85, 81, 81, 85, 79, 91, 25, 33, 66, 16, 55, 36, 72, 80, 7, 69, 87, 8, 3, 35, 36, 79, 30, 15, 93, 68, 98, 87, 58, 99, 28, 95, 42, 97, 18, 5, 9, 84, 9, 18, 56, 15], [79, 78, 62, 35, 40, 51, 60, 56, 84, 75, 41, 54, 17, 25, 93, 87, 9, 56, 89, 23, 2, 45, 65, 38, 6, 48, 44, 79, 7, 66, 62, 30, 93, 76, 52, 98, 94, 36, 35, 66, 50, 3, 76, 4], [55, 52, 59, 71, 20, 19, 8, 67, 27, 79, 8, 18, 29, 46, 36, 3, 9, 10, 84, 66, 1, 91, 4, 48, 96, 18, 78, 45, 15, 51, 61, 4, 19, 88, 94, 77, 11, 28, 57, 75, 54, 65, 47, 4], [34, 76, 54, 88, 61, 96, 83, 93, 93, 83, 20, 3, 40, 69, 23, 69, 94, 32, 24, 51, 58, 42, 35, 32, 54, 45, 48, 86, 85, 92, 49, 34, 16, 11, 97, 19, 92, 29, 54, 53, 67, 82, 82, 76], [82, 32, 83, 56, 63, 4, 11, 3, 27, 80, 44, 18, 30, 88, 70, 47, 34, 76, 42, 23, 40, 15, 80, 57, 14, 79, 12, 35, 25, 78, 2, 18, 35, 9, 11, 90, 67, 69, 96, 74, 38, 70, 75, 81], [59, 66, 41, 24, 50, 5, 21, 6, 4, 9, 69, 68, 9, 18, 59, 43, 80, 66, 29, 48, 51, 42, 36, 76, 45, 98, 35, 6, 37, 36, 84, 16, 72, 22, 69, 69, 63, 75, 19, 81, 18, 73, 17, 41], [33, 84, 55, 82, 24, 77, 40, 28, 67, 75, 39, 21, 37, 2, 6, 52, 5, 47, 43, 96, 40, 11, 81, 14, 2, 39, 63, 63, 18, 97, 94, 79, 93, 90, 1, 17, 54, 39, 48, 66, 15, 22, 20, 93], [89, 43, 56, 24, 98, 43, 21, 48, 66, 16, 40, 21, 52, 8, 78, 55, 86, 82, 58, 5, 42, 30, 95, 9, 95, 95, 41, 51, 57, 73, 61, 6, 26, 74, 6, 53, 61, 33, 45, 94, 40, 24, 92, 45], [38, 29, 79, 8, 64, 87, 73, 51, 75, 6, 47, 49, 76, 98, 85, 32, 54, 36, 89, 99, 98, 19, 37, 17, 80, 16, 58, 44, 68, 49, 94, 51, 98, 5, 97, 58, 46, 55, 73, 17, 12, 24, 56, 55], [76, 79, 16, 87, 82, 22, 44, 95, 43, 79, 21, 8, 49, 6, 81, 47, 36, 92, 23, 31, 75, 62, 84, 96, 81, 57, 70, 65, 37, 68, 95, 75, 17, 7, 52, 35, 2, 40, 37, 57, 10, 76, 81, 46], [90, 5, 5, 27, 5, 61, 8, 31, 97, 21, 99, 21, 51, 79, 59, 2, 30, 58, 92, 81, 20, 40, 29, 5, 89, 10, 83, 61, 1, 47, 98, 57, 14, 25, 90, 21, 16, 74, 32, 45, 64, 84, 73, 60], [98, 95, 19, 47, 95, 64, 30, 47, 88, 33, 82, 21, 95, 63, 42, 61, 43, 68, 26, 33, 33, 49, 84, 41, 72, 36, 72, 95, 22, 47, 83, 20, 87, 24, 43, 88, 73, 16, 27, 45, 37, 13, 51, 2], [76, 97, 87, 59, 14, 49, 30, 98, 9, 79, 24, 41, 60, 89, 32, 47, 21, 42, 70, 89, 2, 31, 56, 30, 63, 15, 18, 32, 14, 62, 82, 99, 52, 22, 14, 78, 34, 86, 80, 56, 53, 49, 63, 16], [80, 40, 38, 18, 23, 48, 82, 46, 22, 54, 40, 30, 55, 56, 42, 42, 62, 82, 53, 82, 53, 64, 1, 79, 69, 27, 17, 63, 41, 58, 57, 96, 38, 90, 66, 92, 45, 23, 20, 36, 42, 22, 60, 11], [28, 45, 22, 81, 63, 31, 11, 36, 78, 35, 23, 29, 23, 16, 84, 89, 19, 90, 96, 63, 50, 85, 73, 43, 19, 85, 18, 6, 35, 14, 64, 9, 35, 2, 6, 99, 25, 73, 50, 95, 7, 63, 28, 2], [65, 59, 24, 62, 99, 71, 38, 93, 62, 65, 51, 94, 52, 96, 74, 98, 63, 11, 48, 54, 91, 50, 74, 38, 86, 88, 8, 6, 68, 69, 6, 32, 38, 57, 84, 64, 54, 14, 64, 50, 47, 54, 19, 75], [39, 65, 99, 83, 60, 33, 32, 36, 24, 43, 71, 71, 46, 47, 69, 14, 45, 52, 90, 50, 65, 77, 64, 23, 84, 71, 70, 59, 73, 92, 74, 54, 99, 71, 89, 94, 26, 44, 76, 13, 54, 40, 4, 53], [1, 6, 55, 66, 91, 18, 29, 53, 33, 3, 20, 4, 82, 8, 86, 86, 83, 28, 66, 73, 99, 86, 26, 34, 71, 94, 49, 89, 49, 73, 27, 65, 33, 72, 49, 63, 32, 19, 50, 22, 90, 67, 9, 35], [71, 79, 4, 37, 28, 9, 35, 25, 9, 61, 52, 97, 17, 76, 9, 54, 5, 63, 47, 90, 19, 99, 66, 45, 71, 73, 86, 33, 80, 43, 88, 72, 94, 26, 45, 35, 81, 53, 10, 41, 17, 71, 66, 11], [63, 67, 46, 20, 13, 87, 17, 93, 32, 99, 99, 98, 85, 16, 23, 11, 14, 67, 71, 45, 75, 33, 83, 45, 54, 51, 87, 23, 29, 6, 39, 5, 96, 40, 90, 78, 82, 21, 59, 89, 20, 24, 3, 86], [72, 57, 93, 71, 70, 70, 76, 63, 86, 47, 90, 89, 19, 99, 13, 89, 45, 32, 30, 85, 42, 72, 42, 7, 3, 37, 3, 18, 42, 9, 57, 24, 7, 97, 89, 42, 98, 58, 85, 56, 58, 18, 39, 50], [33, 28, 56, 25, 14, 55, 84, 84, 7, 4, 95, 30, 62, 57, 37, 55, 85, 65, 52, 3, 77, 7, 70, 70, 34, 96, 16, 8, 21, 11, 50, 87, 6, 15, 11, 27, 79, 45, 38, 4, 78, 45, 10, 54], [29, 12, 56, 40, 84, 37, 66, 20, 12, 38, 30, 47, 82, 74, 71, 42, 5, 48, 93, 99, 51, 12, 10, 37, 66, 67, 14, 47, 20, 52, 68, 26, 47, 79, 73, 3, 2, 41, 30, 37, 81, 3, 9, 8], [9, 17, 24, 72, 14, 54, 80, 18, 88, 39, 47, 27, 92, 71, 98, 91, 34, 19, 6, 30, 92, 12, 15, 39, 64, 64, 15, 58, 67, 1, 7, 9, 1, 5, 47, 10, 2, 23, 93, 56, 19, 38, 47, 84]],33,),
    ([[99, 52, 49, 71, 23, 50, 17, 48, 2, 69, 62], [85, 13, 61, 11, 88, 97, 27, 35, 18, 85, 68], [61, 41, 96, 43, 49, 11, 67, 51, 52, 85, 43], [58, 78, 70, 29, 31, 28, 50, 36, 92, 19, 67], [12, 88, 76, 24, 65, 92, 80, 21, 94, 98, 26], [35, 95, 80, 58, 42, 29, 29, 9, 78, 72, 2], [75, 2, 18, 69, 57, 71, 23, 19, 19, 58, 83], [49, 45, 28, 75, 50, 11, 55, 9, 14, 98, 93], [21, 48, 58, 69, 97, 9, 67, 78, 18, 12, 87], [78, 16, 37, 20, 20, 15, 25, 17, 12, 42, 39], [56, 53, 71, 72, 88, 47, 25, 85, 50, 33, 74]],10,),
    ([[29, 3, 39, 4, 37, 95, 6, 92, 10, 12, 66, 3, 65, 64, 35, 24, 47, 52, 34], [84, 80, 94, 25, 69, 29, 92, 64, 53, 58, 41, 87, 96, 51, 18, 41, 99, 61, 24], [47, 28, 36, 21, 56, 69, 26, 54, 87, 44, 33, 26, 22, 20, 2, 41, 54, 57, 18], [5, 96, 46, 75, 21, 22, 3, 9, 2, 28, 34, 53, 59, 10, 83, 93, 2, 48, 6], [44, 54, 71, 36, 8, 83, 10, 33, 91, 93, 19, 18, 51, 23, 1, 59, 3, 10, 71], [49, 56, 90, 16, 39, 96, 76, 44, 8, 8, 45, 11, 97, 25, 17, 95, 83, 55, 79], [56, 44, 53, 35, 39, 2, 98, 25, 38, 68, 80, 32, 79, 78, 41, 79, 71, 7, 72], [83, 18, 17, 82, 83, 77, 59, 11, 51, 7, 27, 59, 37, 5, 62, 72, 74, 90, 79], [55, 16, 93, 92, 74, 56, 51, 68, 46, 61, 78, 33, 55, 18, 12, 74, 21, 97, 78], [73, 26, 79, 21, 22, 55, 46, 41, 5, 44, 16, 35, 5, 62, 90, 26, 61, 51, 69], [56, 50, 36, 24, 79, 30, 69, 48, 22, 33, 69, 96, 50, 23, 10, 36, 17, 53, 91], [8, 44, 61, 6, 71, 90, 81, 37, 54, 23, 91, 57, 51, 58, 19, 27, 89, 25, 21], [25, 51, 71, 35, 70, 50, 15, 24, 49, 68, 7, 94, 81, 54, 38, 94, 45, 9, 55], [83, 52, 77, 49, 55, 83, 70, 76, 79, 3, 68, 38, 70, 49, 92, 8, 95, 85, 45], [29, 79, 49, 24, 21, 23, 95, 98, 28, 32, 22, 62, 67, 73, 6, 65, 22, 51, 68], [57, 72, 55, 42, 52, 61, 19, 1, 41, 63, 88, 48, 81, 32, 50, 14, 17, 96, 97], [30, 51, 98, 92, 62, 24, 63, 14, 34, 59, 65, 86, 33, 58, 18, 12, 74, 66, 2], [70, 84, 28, 42, 3, 48, 89, 87, 13, 57, 88, 3, 63, 38, 59, 28, 26, 84, 91], [65, 74, 74, 61, 57, 1, 32, 32, 27, 13, 17, 28, 89, 52, 36, 47, 66, 32, 32]],0,),
    ([[55, 73, 80, 89, 40, 28, 81, 31, 87, 31, 26, 4, 58, 79, 23, 69, 60, 43, 89, 94, 26, 67, 68, 55, 47, 82, 59, 75, 75, 16, 58], [89, 1, 90, 45, 94, 6, 91, 52, 19, 43, 19, 39, 32, 65, 89, 47, 13, 74, 82, 36, 86, 70, 27, 72, 24, 20, 86, 9, 39, 83, 1], [11, 74, 1, 91, 81, 44, 51, 17, 66, 23, 41, 59, 74, 94, 99, 25, 17, 19, 82, 82, 46, 35, 74, 23, 86, 44, 9, 32, 90, 93, 59], [42, 62, 19, 93, 35, 76, 8, 89, 91, 43, 45, 6, 13, 11, 70, 69, 7, 55, 55, 19, 6, 89, 9, 20, 25, 50, 72, 50, 38, 66, 57], [22, 56, 36, 51, 68, 1, 48, 33, 24, 49, 69, 58, 48, 57, 64, 99, 53, 60, 90, 43, 41, 26, 59, 49, 64, 5, 44, 18, 57, 89, 40], [46, 58, 85, 24, 28, 46, 68, 72, 54, 33, 67, 84, 35, 39, 47, 71, 91, 5, 37, 1, 86, 56, 7, 64, 8, 94, 64, 57, 28, 26, 34], [96, 22, 20, 14, 23, 67, 19, 78, 39, 37, 99, 1, 19, 15, 89, 1, 31, 52, 43, 46, 86, 50, 20, 62, 43, 5, 79, 66, 12, 57, 60], [55, 71, 66, 72, 73, 27, 28, 37, 79, 19, 94, 51, 13, 45, 6, 94, 1, 25, 99, 26, 13, 19, 10, 45, 71, 15, 87, 31, 8, 30, 98], [97, 1, 16, 11, 27, 86, 40, 83, 44, 70, 57, 48, 40, 39, 84, 3, 55, 1, 23, 67, 62, 34, 17, 48, 91, 53, 61, 87, 11, 15, 90], [11, 7, 47, 8, 5, 81, 87, 66, 91, 63, 21, 71, 90, 94, 12, 11, 54, 81, 10, 16, 15, 58, 79, 84, 4, 96, 22, 35, 14, 94, 31], [74, 70, 91, 11, 36, 74, 80, 24, 85, 40, 42, 87, 21, 96, 81, 51, 81, 55, 85, 4, 62, 87, 25, 96, 70, 14, 41, 57, 38, 62, 41], [45, 80, 96, 16, 19, 37, 85, 79, 61, 26, 94, 79, 64, 13, 91, 87, 34, 98, 23, 20, 54, 73, 58, 59, 20, 39, 78, 90, 91, 98, 93], [32, 41, 69, 68, 87, 21, 97, 24, 16, 32, 83, 26, 3, 99, 82, 7, 96, 88, 16, 53, 88, 4, 45, 32, 98, 83, 78, 58, 13, 22, 95], [44, 44, 30, 23, 12, 14, 36, 45, 72, 24, 3, 78, 51, 75, 55, 38, 92, 87, 82, 20, 97, 2, 26, 2, 67, 84, 74, 42, 85, 40, 9], [2, 28, 3, 16, 4, 23, 94, 77, 6, 74, 55, 81, 8, 73, 98, 81, 86, 64, 67, 41, 40, 93, 27, 39, 53, 40, 52, 37, 67, 19, 34], [78, 85, 66, 10, 52, 42, 60, 81, 2, 91, 1, 50, 36, 97, 22, 99, 98, 82, 36, 3, 44, 16, 11, 10, 51, 42, 85, 25, 99, 6, 44], [8, 34, 41, 1, 3, 52, 91, 77, 43, 47, 83, 19, 70, 47, 78, 5, 64, 45, 64, 45, 36, 9, 23, 32, 93, 45, 28, 52, 11, 19, 64], [65, 73, 57, 66, 4, 29, 4, 1, 92, 18, 13, 70, 49, 47, 86, 30, 27, 72, 28, 2, 20, 75, 78, 24, 77, 72, 44, 21, 22, 73, 58], [11, 80, 53, 9, 67, 52, 13, 1, 44, 75, 24, 5, 66, 81, 81, 20, 64, 15, 68, 54, 11, 23, 1, 42, 47, 68, 38, 2, 45, 27, 98], [77, 61, 82, 11, 69, 29, 25, 78, 54, 48, 46, 41, 41, 61, 11, 44, 32, 49, 6, 57, 6, 47, 63, 49, 22, 67, 19, 55, 34, 41, 7], [57, 16, 59, 38, 9, 77, 34, 46, 37, 43, 47, 6, 38, 61, 4, 5, 70, 60, 77, 88, 92, 77, 56, 82, 59, 7, 68, 31, 88, 86, 85], [48, 42, 90, 30, 51, 35, 62, 51, 87, 50, 30, 19, 96, 50, 54, 83, 86, 4, 12, 15, 15, 10, 61, 19, 53, 72, 57, 95, 9, 29, 7], [72, 17, 79, 16, 71, 83, 38, 89, 76, 96, 47, 10, 24, 50, 68, 43, 37, 45, 54, 43, 68, 37, 89, 41, 94, 1, 93, 16, 37, 37, 7], [40, 51, 64, 97, 22, 43, 62, 54, 27, 29, 16, 85, 11, 21, 9, 27, 86, 79, 23, 51, 93, 80, 3, 16, 8, 90, 42, 73, 35, 71, 72], [99, 48, 54, 36, 6, 71, 12, 59, 65, 50, 43, 43, 49, 89, 76, 55, 91, 87, 83, 85, 50, 21, 88, 13, 42, 15, 50, 1, 51, 34, 42], [62, 95, 32, 61, 93, 54, 74, 58, 85, 24, 27, 21, 18, 55, 68, 47, 54, 18, 73, 64, 49, 94, 35, 94, 39, 58, 57, 6, 78, 93, 96], [78, 20, 50, 9, 76, 14, 23, 48, 98, 80, 82, 56, 40, 97, 69, 39, 74, 86, 43, 97, 31, 70, 3, 4, 27, 89, 27, 47, 60, 36, 46], [61, 42, 7, 30, 50, 47, 93, 40, 5, 70, 58, 44, 71, 32, 79, 77, 82, 74, 40, 57, 11, 40, 47, 2, 91, 52, 72, 49, 59, 38, 16], [88, 87, 78, 27, 74, 28, 89, 66, 45, 33, 60, 50, 46, 35, 41, 58, 77, 55, 5, 5, 22, 34, 65, 59, 17, 51, 49, 9, 74, 15, 29], [53, 25, 85, 81, 91, 28, 23, 3, 33, 71, 69, 90, 17, 81, 67, 67, 34, 8, 45, 60, 56, 70, 22, 33, 50, 71, 83, 46, 52, 74, 87], [66, 21, 24, 48, 13, 64, 5, 18, 75, 37, 54, 32, 28, 86, 45, 28, 65, 70, 75, 42, 33, 16, 13, 21, 59, 47, 39, 88, 43, 27, 37]],16,),
    ([[76, 7, 58], [20, 79, 65], [74, 14, 79]],2,),
    ([[89, 95, 74, 37, 6, 6, 28, 78, 13, 13, 10, 80, 39, 99, 79, 23, 37, 8, 90, 60, 86, 5, 98, 27, 19, 43, 43, 35, 84, 55, 61, 47, 77, 56, 82, 18, 65, 96, 53, 89, 85, 91, 11, 1, 83, 96, 8, 19, 55], [16, 99, 66, 12, 93, 74, 62, 86, 98, 58, 21, 37, 5, 70, 32, 67, 10, 69, 88, 84, 62, 37, 95, 47, 81, 49, 24, 82, 26, 55, 7, 78, 41, 2, 30, 81, 20, 56, 74, 24, 12, 91, 15, 73, 82, 48, 61, 71, 28], [3, 16, 36, 4, 99, 9, 12, 74, 44, 66, 19, 13, 55, 97, 65, 92, 70, 3, 25, 52, 16, 43, 56, 68, 8, 80, 44, 38, 23, 6, 43, 44, 80, 80, 23, 16, 76, 9, 82, 9, 85, 58, 65, 59, 23, 69, 19, 35, 97], [55, 82, 40, 14, 84, 13, 53, 80, 95, 39, 99, 84, 65, 56, 40, 46, 77, 7, 45, 22, 7, 84, 52, 68, 70, 67, 3, 58, 67, 54, 9, 54, 80, 51, 16, 12, 20, 53, 31, 94, 21, 3, 21, 92, 28, 5, 71, 69, 73], [47, 85, 20, 38, 37, 58, 17, 42, 92, 95, 97, 32, 62, 96, 87, 21, 89, 33, 67, 6, 92, 66, 32, 64, 26, 62, 5, 11, 74, 79, 82, 49, 78, 92, 94, 62, 60, 77, 84, 2, 89, 59, 76, 25, 68, 42, 76, 71, 55], [38, 96, 43, 70, 53, 91, 99, 21, 20, 19, 33, 63, 68, 60, 19, 28, 22, 51, 88, 63, 62, 94, 29, 74, 32, 73, 25, 16, 15, 59, 48, 18, 23, 55, 42, 3, 71, 52, 11, 55, 88, 99, 25, 92, 76, 87, 81, 41, 37], [82, 55, 9, 99, 36, 57, 63, 82, 20, 85, 47, 20, 6, 73, 93, 29, 77, 91, 49, 6, 39, 32, 49, 43, 28, 45, 65, 50, 54, 51, 43, 64, 95, 30, 82, 93, 42, 38, 87, 86, 66, 69, 15, 61, 96, 6, 78, 24, 85], [14, 12, 55, 68, 44, 85, 81, 93, 51, 80, 82, 38, 41, 44, 75, 96, 92, 16, 98, 50, 94, 38, 86, 5, 9, 77, 39, 87, 27, 32, 64, 95, 33, 90, 18, 76, 67, 5, 78, 59, 76, 4, 16, 75, 48, 66, 77, 8, 44], [21, 26, 35, 15, 40, 30, 66, 80, 13, 1, 43, 28, 1, 40, 34, 13, 61, 66, 4, 89, 98, 13, 36, 96, 61, 58, 85, 90, 15, 93, 90, 85, 12, 76, 69, 61, 42, 90, 32, 2, 8, 91, 54, 8, 88, 13, 29, 13, 58], [63, 87, 47, 79, 88, 87, 74, 38, 69, 69, 95, 40, 1, 2, 29, 7, 93, 57, 55, 73, 36, 7, 92, 10, 80, 74, 39, 58, 90, 98, 98, 40, 14, 82, 1, 17, 49, 86, 16, 7, 15, 21, 66, 59, 48, 89, 73, 84, 50], [10, 52, 85, 68, 30, 34, 94, 78, 86, 65, 60, 8, 75, 65, 69, 57, 45, 49, 74, 62, 39, 77, 21, 53, 45, 97, 28, 53, 9, 75, 93, 71, 61, 27, 22, 95, 30, 92, 84, 15, 15, 53, 76, 81, 23, 70, 16, 91, 87], [65, 45, 7, 45, 39, 50, 49, 48, 49, 40, 39, 57, 82, 63, 56, 86, 2, 26, 96, 23, 18, 83, 88, 68, 60, 2, 94, 49, 38, 31, 40, 80, 53, 64, 33, 58, 50, 64, 3, 61, 82, 10, 66, 51, 94, 30, 25, 43, 88], [64, 59, 62, 99, 10, 64, 94, 60, 90, 99, 88, 20, 49, 99, 74, 27, 51, 57, 79, 79, 37, 99, 3, 29, 68, 47, 80, 69, 21, 42, 21, 2, 78, 69, 7, 75, 35, 30, 44, 46, 55, 1, 54, 80, 1, 63, 55, 86, 77], [27, 15, 81, 9, 69, 59, 23, 11, 24, 72, 98, 54, 31, 22, 14, 5, 17, 82, 83, 71, 90, 89, 82, 44, 79, 93, 49, 65, 4, 9, 36, 51, 32, 88, 18, 15, 20, 58, 40, 66, 89, 13, 91, 13, 62, 28, 46, 15, 93], [85, 44, 95, 23, 67, 99, 78, 66, 50, 13, 2, 76, 91, 34, 40, 69, 61, 25, 75, 77, 63, 28, 85, 56, 26, 27, 26, 15, 50, 6, 68, 4, 30, 77, 9, 42, 14, 92, 40, 3, 41, 93, 33, 79, 60, 64, 62, 79, 7], [76, 50, 39, 71, 47, 70, 26, 58, 73, 51, 88, 52, 94, 16, 48, 27, 33, 23, 45, 83, 83, 22, 42, 33, 10, 47, 96, 79, 39, 46, 72, 51, 25, 82, 15, 58, 59, 26, 41, 44, 85, 22, 98, 37, 14, 4, 24, 66, 63], [65, 66, 13, 27, 81, 17, 69, 88, 57, 72, 73, 18, 16, 51, 96, 40, 39, 56, 54, 44, 46, 32, 48, 61, 66, 38, 43, 4, 5, 58, 37, 26, 9, 15, 88, 88, 99, 89, 26, 63, 87, 70, 27, 54, 83, 31, 32, 2, 18], [28, 71, 87, 88, 92, 25, 39, 49, 4, 52, 83, 68, 57, 13, 65, 63, 98, 71, 25, 23, 30, 61, 7, 54, 17, 97, 60, 66, 38, 13, 52, 52, 32, 86, 9, 17, 82, 40, 91, 75, 54, 54, 28, 72, 50, 18, 13, 33, 15], [86, 38, 94, 6, 45, 59, 98, 83, 97, 78, 48, 41, 83, 79, 74, 55, 61, 2, 2, 85, 76, 10, 76, 39, 2, 65, 66, 87, 92, 81, 52, 85, 44, 34, 73, 81, 45, 32, 5, 78, 89, 86, 63, 69, 54, 38, 9, 61, 95], [21, 36, 1, 22, 87, 87, 15, 46, 65, 6, 40, 35, 81, 61, 23, 20, 28, 37, 82, 7, 49, 84, 24, 80, 13, 92, 7, 15, 87, 23, 95, 69, 91, 60, 10, 51, 64, 71, 56, 32, 23, 54, 73, 93, 91, 85, 70, 90, 84], [61, 79, 20, 53, 15, 29, 70, 80, 65, 62, 70, 16, 54, 97, 7, 60, 10, 53, 8, 85, 90, 37, 82, 4, 84, 83, 97, 23, 9, 38, 45, 45, 18, 46, 2, 48, 17, 16, 45, 48, 24, 95, 65, 92, 33, 4, 1, 33, 74], [62, 3, 45, 21, 64, 73, 57, 40, 62, 43, 88, 46, 72, 24, 24, 10, 99, 68, 57, 44, 73, 75, 48, 77, 27, 30, 46, 12, 60, 19, 68, 54, 34, 87, 90, 7, 82, 42, 68, 53, 8, 22, 26, 77, 63, 46, 81, 44, 62], [36, 41, 79, 82, 27, 70, 98, 41, 5, 57, 76, 29, 12, 25, 34, 75, 87, 24, 82, 63, 63, 10, 5, 95, 89, 53, 81, 28, 65, 45, 66, 49, 40, 66, 91, 8, 27, 17, 68, 44, 31, 5, 60, 89, 92, 19, 42, 23, 77], [17, 94, 58, 87, 49, 3, 77, 96, 45, 35, 2, 47, 3, 29, 74, 20, 34, 79, 40, 65, 90, 63, 56, 32, 66, 96, 41, 29, 84, 87, 51, 12, 44, 10, 83, 74, 83, 90, 88, 9, 29, 29, 92, 61, 64, 3, 87, 4, 55], [14, 77, 28, 63, 39, 64, 60, 20, 28, 96, 14, 77, 75, 58, 39, 58, 15, 73, 3, 5, 92, 42, 15, 3, 35, 7, 94, 24, 31, 78, 80, 4, 3, 99, 9, 68, 83, 88, 60, 11, 79, 36, 95, 72, 2, 50, 3, 67, 85], [62, 76, 14, 23, 77, 16, 81, 18, 13, 56, 90, 45, 40, 31, 81, 32, 1, 35, 36, 83, 92, 66, 29, 43, 29, 43, 19, 64, 92, 98, 31, 19, 96, 29, 73, 7, 58, 76, 60, 51, 95, 82, 92, 50, 21, 9, 34, 34, 47], [24, 80, 28, 46, 51, 99, 6, 63, 53, 64, 52, 60, 41, 11, 4, 14, 13, 15, 8, 88, 11, 99, 89, 23, 7, 69, 32, 92, 44, 3, 94, 44, 69, 51, 61, 51, 33, 20, 30, 44, 86, 86, 29, 21, 82, 53, 11, 10, 35], [26, 44, 4, 74, 57, 39, 80, 41, 94, 67, 98, 89, 36, 4, 74, 13, 70, 7, 28, 59, 37, 15, 30, 74, 12, 81, 30, 1, 36, 88, 21, 32, 63, 82, 13, 37, 44, 21, 18, 46, 47, 26, 5, 5, 31, 28, 77, 75, 65], [88, 13, 18, 24, 29, 28, 45, 86, 84, 11, 51, 59, 84, 13, 47, 88, 43, 24, 48, 63, 17, 69, 54, 94, 14, 15, 73, 78, 10, 22, 95, 13, 81, 65, 14, 44, 39, 35, 65, 27, 45, 57, 22, 34, 9, 50, 54, 58, 96], [62, 38, 84, 27, 64, 3, 11, 24, 29, 69, 97, 8, 19, 68, 99, 94, 69, 48, 40, 67, 16, 64, 8, 5, 99, 72, 25, 53, 49, 72, 21, 51, 46, 9, 64, 96, 77, 23, 60, 59, 8, 64, 99, 54, 92, 15, 52, 93, 51], [4, 34, 24, 21, 2, 7, 56, 75, 76, 68, 35, 26, 18, 64, 56, 80, 55, 12, 37, 52, 19, 15, 86, 84, 52, 77, 87, 95, 26, 45, 96, 21, 81, 93, 53, 29, 48, 86, 19, 54, 78, 87, 2, 32, 62, 97, 7, 98, 68], [87, 84, 22, 29, 3, 22, 84, 89, 98, 53, 93, 57, 10, 40, 20, 87, 11, 8, 93, 36, 25, 39, 98, 96, 62, 87, 21, 19, 25, 87, 83, 5, 83, 99, 12, 25, 5, 76, 27, 4, 83, 45, 47, 88, 28, 97, 35, 16, 12], [80, 75, 43, 28, 87, 81, 19, 75, 68, 74, 55, 83, 36, 62, 39, 41, 60, 86, 66, 59, 97, 40, 91, 19, 55, 46, 4, 83, 62, 25, 63, 70, 13, 86, 4, 2, 67, 30, 4, 48, 43, 93, 45, 97, 13, 47, 96, 28, 37], [28, 27, 89, 30, 6, 94, 9, 6, 29, 87, 70, 86, 66, 95, 53, 70, 5, 20, 12, 8, 58, 49, 64, 50, 97, 39, 40, 31, 3, 83, 72, 30, 95, 29, 70, 56, 66, 87, 63, 30, 53, 46, 9, 7, 63, 47, 44, 49, 79], [79, 85, 62, 59, 78, 75, 75, 84, 13, 30, 84, 43, 51, 8, 37, 97, 90, 64, 39, 8, 62, 82, 39, 14, 52, 82, 57, 21, 23, 4, 74, 43, 11, 84, 19, 65, 95, 2, 49, 69, 34, 4, 91, 39, 49, 3, 26, 41, 65], [16, 58, 35, 83, 16, 33, 31, 22, 61, 84, 64, 70, 35, 39, 3, 96, 13, 14, 41, 8, 19, 14, 75, 50, 99, 61, 36, 67, 89, 77, 80, 92, 45, 91, 74, 82, 72, 7, 22, 9, 60, 42, 59, 40, 29, 55, 64, 42, 29], [92, 21, 97, 63, 63, 90, 38, 79, 66, 12, 33, 79, 1, 97, 68, 28, 62, 78, 59, 49, 45, 76, 6, 20, 85, 16, 12, 52, 20, 58, 45, 97, 2, 34, 26, 33, 42, 94, 65, 8, 65, 10, 32, 51, 57, 40, 66, 31, 63], [68, 56, 12, 31, 23, 33, 8, 62, 80, 15, 41, 52, 26, 78, 12, 27, 95, 68, 30, 4, 54, 95, 34, 68, 84, 56, 18, 47, 72, 60, 59, 2, 73, 16, 86, 58, 12, 5, 39, 15, 72, 88, 19, 82, 85, 49, 39, 78, 15], [55, 67, 56, 45, 75, 57, 67, 94, 6, 70, 31, 22, 85, 38, 58, 70, 29, 56, 11, 48, 86, 60, 51, 39, 6, 30, 89, 1, 86, 9, 45, 8, 34, 80, 83, 8, 12, 43, 56, 31, 42, 33, 19, 91, 88, 92, 55, 4, 12], [87, 84, 28, 58, 48, 1, 75, 44, 63, 95, 38, 9, 6, 70, 52, 67, 96, 99, 16, 2, 36, 71, 35, 30, 45, 46, 93, 65, 1, 57, 71, 67, 31, 25, 47, 56, 88, 1, 95, 37, 75, 67, 12, 20, 30, 74, 64, 79, 85], [64, 18, 32, 19, 94, 33, 62, 22, 29, 88, 4, 50, 76, 4, 5, 83, 39, 57, 31, 7, 12, 10, 29, 85, 13, 87, 70, 31, 9, 51, 88, 16, 59, 58, 11, 36, 1, 21, 44, 37, 6, 14, 93, 1, 8, 44, 83, 87, 75], [27, 36, 42, 20, 8, 46, 52, 26, 35, 60, 3, 4, 93, 62, 64, 50, 92, 19, 43, 92, 82, 14, 14, 54, 29, 3, 98, 73, 5, 93, 5, 45, 64, 64, 43, 43, 51, 13, 90, 73, 68, 95, 69, 7, 92, 78, 88, 42, 5], [47, 48, 98, 92, 47, 8, 21, 88, 24, 13, 15, 89, 53, 92, 72, 31, 71, 51, 47, 39, 81, 57, 50, 57, 35, 86, 7, 53, 10, 92, 39, 58, 93, 35, 59, 22, 9, 8, 94, 94, 58, 95, 22, 95, 40, 28, 46, 69, 81], [52, 11, 22, 47, 89, 13, 45, 75, 69, 78, 22, 67, 35, 32, 38, 58, 40, 88, 92, 21, 49, 97, 92, 39, 61, 10, 40, 58, 89, 45, 17, 68, 10, 62, 89, 32, 72, 42, 45, 76, 21, 27, 30, 74, 85, 1, 9, 3, 53], [42, 19, 6, 7, 43, 80, 36, 68, 82, 96, 96, 82, 39, 43, 37, 28, 50, 39, 2, 37, 66, 19, 69, 44, 13, 22, 7, 2, 62, 78, 89, 90, 5, 20, 54, 76, 63, 36, 95, 81, 16, 57, 64, 10, 99, 97, 99, 51, 27], [7, 91, 41, 76, 97, 13, 66, 3, 11, 5, 60, 2, 92, 77, 99, 64, 13, 54, 12, 18, 18, 17, 39, 86, 13, 45, 19, 88, 19, 21, 24, 30, 92, 48, 35, 59, 17, 48, 98, 55, 9, 77, 14, 26, 52, 85, 44, 84, 11], [51, 42, 62, 35, 64, 95, 18, 14, 49, 69, 17, 21, 14, 3, 31, 89, 47, 44, 17, 90, 81, 56, 83, 27, 71, 90, 69, 2, 80, 62, 75, 87, 99, 6, 65, 97, 18, 55, 67, 57, 19, 74, 84, 11, 96, 84, 55, 96, 37], [86, 4, 13, 70, 93, 58, 2, 60, 89, 32, 63, 60, 26, 90, 22, 74, 87, 4, 16, 63, 42, 33, 13, 46, 13, 33, 14, 8, 90, 86, 46, 1, 59, 60, 49, 80, 93, 61, 23, 5, 85, 50, 36, 20, 43, 8, 90, 41, 25], [7, 86, 61, 33, 69, 38, 12, 44, 53, 14, 71, 92, 52, 52, 46, 80, 41, 2, 49, 95, 78, 28, 32, 92, 76, 77, 22, 42, 29, 94, 79, 68, 33, 46, 9, 38, 80, 26, 43, 53, 27, 11, 26, 78, 57, 1, 11, 30, 88]],41,),
    ([[4, 86, 72, 80, 33, 33, 74, 66, 4, 87, 51, 27, 33, 97, 84, 77, 75, 83, 32, 67, 77, 28, 86, 57, 19, 31, 84, 53, 88, 32, 9, 51, 83, 23, 25, 97, 46, 44, 66, 67, 28, 99, 78, 24, 56, 50, 3, 23, 34], [9, 82, 59, 66, 22, 35, 31, 90, 78, 48, 53, 92, 75, 32, 85, 87, 88, 12, 62, 3, 6, 12, 53, 20, 6, 84, 14, 56, 41, 49, 65, 84, 86, 95, 31, 28, 12, 16, 97, 35, 44, 68, 10, 98, 3, 31, 52, 95, 65], [5, 5, 66, 15, 65, 21, 71, 11, 90, 42, 66, 94, 61, 60, 14, 5, 31, 48, 32, 57, 34, 74, 95, 27, 82, 5, 17, 75, 69, 56, 38, 54, 48, 85, 88, 94, 80, 49, 41, 22, 57, 66, 19, 2, 75, 33, 73, 59, 89], [6, 11, 27, 72, 45, 31, 91, 63, 44, 41, 47, 69, 79, 2, 15, 95, 20, 3, 39, 74, 90, 10, 40, 13, 85, 98, 44, 32, 73, 30, 1, 53, 76, 44, 35, 88, 40, 45, 60, 63, 10, 47, 24, 57, 18, 57, 72, 46, 43], [77, 16, 14, 9, 73, 69, 61, 11, 19, 64, 38, 10, 16, 93, 69, 82, 42, 44, 53, 35, 36, 22, 24, 76, 12, 35, 50, 83, 78, 87, 40, 22, 47, 75, 66, 10, 43, 69, 94, 85, 97, 25, 47, 7, 28, 80, 45, 67, 83], [12, 83, 11, 3, 61, 66, 56, 26, 86, 81, 34, 55, 79, 76, 16, 80, 39, 6, 72, 52, 25, 56, 83, 19, 76, 73, 93, 27, 5, 26, 30, 78, 97, 35, 75, 53, 68, 33, 70, 28, 74, 36, 49, 90, 94, 86, 53, 69, 2], [97, 80, 71, 64, 21, 35, 46, 86, 48, 22, 6, 33, 39, 43, 25, 18, 41, 35, 24, 55, 40, 87, 97, 29, 10, 79, 10, 90, 64, 29, 98, 18, 2, 25, 85, 51, 95, 22, 9, 91, 89, 89, 91, 74, 94, 4, 21, 30, 33], [43, 90, 2, 87, 31, 4, 47, 84, 89, 45, 65, 66, 6, 7, 51, 68, 18, 41, 69, 25, 56, 1, 98, 55, 3, 54, 81, 32, 88, 2, 65, 98, 8, 58, 53, 44, 73, 28, 19, 56, 20, 71, 56, 35, 19, 81, 63, 82, 7], [27, 39, 30, 23, 84, 23, 90, 47, 78, 48, 95, 91, 63, 9, 23, 63, 74, 47, 87, 74, 66, 37, 38, 1, 48, 82, 35, 71, 86, 53, 25, 42, 23, 9, 27, 75, 51, 91, 92, 57, 82, 36, 34, 13, 55, 46, 52, 94, 28], [86, 88, 30, 45, 38, 20, 70, 97, 47, 59, 79, 79, 96, 14, 42, 61, 59, 8, 57, 22, 84, 88, 21, 28, 49, 23, 88, 54, 23, 68, 46, 68, 94, 28, 95, 97, 50, 83, 63, 10, 89, 37, 13, 70, 30, 87, 80, 72, 80], [11, 1, 86, 18, 11, 84, 10, 48, 61, 10, 60, 22, 75, 99, 9, 15, 83, 37, 70, 44, 69, 3, 10, 77, 4, 56, 40, 33, 98, 33, 60, 21, 69, 45, 57, 77, 40, 81, 64, 10, 74, 66, 85, 65, 30, 82, 35, 53, 39], [22, 67, 70, 80, 67, 75, 17, 19, 60, 72, 78, 90, 89, 51, 48, 57, 10, 32, 79, 68, 28, 4, 61, 77, 12, 15, 29, 87, 13, 38, 58, 35, 40, 76, 94, 5, 2, 30, 99, 10, 73, 81, 38, 59, 94, 35, 71, 12, 42], [98, 49, 67, 33, 13, 75, 20, 95, 33, 34, 50, 50, 9, 7, 9, 26, 2, 5, 66, 10, 31, 33, 6, 14, 78, 15, 97, 95, 81, 43, 79, 20, 21, 64, 29, 59, 73, 64, 93, 44, 34, 47, 9, 60, 30, 17, 52, 59, 4], [40, 96, 96, 7, 38, 32, 69, 67, 56, 20, 64, 17, 16, 11, 13, 18, 14, 34, 76, 86, 85, 26, 42, 61, 39, 2, 57, 50, 16, 62, 98, 11, 83, 63, 30, 54, 71, 27, 86, 64, 81, 79, 9, 76, 72, 2, 49, 48, 55], [80, 67, 31, 26, 66, 30, 77, 78, 1, 96, 70, 22, 75, 87, 54, 14, 14, 84, 71, 19, 26, 59, 22, 6, 63, 77, 74, 54, 19, 95, 10, 37, 77, 17, 55, 5, 21, 39, 20, 71, 15, 79, 53, 87, 33, 44, 66, 50, 32], [79, 71, 73, 55, 28, 86, 3, 53, 42, 2, 22, 25, 89, 32, 7, 62, 31, 63, 37, 68, 97, 79, 9, 70, 46, 95, 34, 60, 13, 36, 96, 86, 48, 93, 75, 6, 5, 65, 50, 74, 74, 24, 7, 86, 58, 21, 86, 33, 44], [25, 95, 80, 15, 29, 83, 52, 17, 90, 36, 35, 40, 23, 73, 34, 58, 82, 80, 61, 96, 28, 60, 32, 58, 82, 44, 34, 93, 21, 1, 55, 80, 49, 97, 21, 99, 55, 27, 20, 95, 16, 78, 48, 32, 32, 53, 53, 2, 57], [22, 52, 81, 96, 81, 58, 34, 71, 93, 17, 88, 72, 23, 33, 29, 19, 69, 37, 87, 26, 24, 54, 21, 97, 90, 10, 42, 29, 57, 35, 28, 12, 58, 44, 7, 16, 84, 93, 35, 92, 7, 86, 14, 59, 62, 74, 66, 22, 16], [99, 75, 43, 97, 98, 97, 83, 20, 10, 19, 12, 10, 71, 56, 11, 80, 97, 61, 38, 17, 54, 45, 25, 31, 65, 39, 20, 73, 43, 66, 1, 55, 51, 5, 12, 14, 60, 96, 40, 9, 42, 42, 33, 25, 78, 9, 91, 44, 83], [58, 25, 32, 22, 93, 55, 92, 61, 57, 77, 61, 92, 67, 94, 75, 2, 57, 73, 33, 90, 63, 16, 89, 1, 85, 64, 84, 69, 17, 40, 1, 13, 18, 68, 14, 5, 62, 33, 26, 61, 68, 30, 62, 62, 81, 92, 70, 57, 91], [36, 7, 65, 74, 77, 41, 32, 14, 33, 30, 73, 6, 10, 75, 20, 89, 12, 22, 76, 14, 48, 54, 36, 61, 55, 14, 2, 2, 61, 6, 25, 67, 23, 73, 95, 28, 25, 99, 65, 66, 79, 43, 40, 80, 23, 49, 99, 8, 7], [21, 35, 97, 99, 82, 61, 83, 74, 68, 30, 97, 68, 9, 17, 43, 88, 57, 13, 57, 26, 61, 62, 19, 81, 30, 90, 13, 49, 82, 85, 98, 51, 9, 94, 29, 93, 83, 8, 81, 76, 15, 69, 34, 52, 50, 67, 5, 98, 9], [88, 5, 27, 84, 47, 62, 45, 66, 23, 98, 61, 93, 43, 35, 30, 67, 10, 56, 34, 65, 6, 70, 43, 16, 63, 65, 5, 25, 27, 42, 55, 26, 16, 90, 28, 92, 30, 77, 89, 45, 19, 13, 75, 23, 14, 74, 98, 23, 40], [64, 85, 59, 20, 32, 78, 24, 46, 18, 94, 92, 48, 14, 54, 21, 98, 5, 31, 67, 87, 59, 44, 64, 94, 42, 94, 38, 7, 59, 69, 70, 49, 78, 11, 2, 95, 27, 16, 64, 66, 49, 90, 16, 73, 52, 73, 5, 36, 7], [61, 96, 29, 67, 30, 40, 31, 48, 91, 6, 62, 29, 9, 54, 84, 11, 19, 74, 5, 87, 70, 95, 18, 21, 15, 59, 95, 74, 6, 24, 97, 60, 28, 92, 74, 23, 79, 46, 37, 14, 48, 78, 71, 36, 82, 60, 54, 79, 63], [97, 48, 22, 43, 41, 17, 63, 90, 79, 18, 72, 3, 54, 14, 34, 97, 1, 48, 99, 10, 83, 11, 99, 66, 3, 15, 59, 64, 47, 92, 2, 30, 38, 5, 6, 5, 12, 4, 24, 25, 26, 55, 46, 46, 43, 60, 33, 21, 87], [37, 12, 21, 13, 33, 70, 76, 61, 30, 37, 82, 16, 45, 71, 1, 53, 28, 53, 44, 67, 39, 10, 51, 14, 79, 6, 39, 80, 82, 99, 48, 25, 97, 33, 83, 75, 67, 65, 40, 25, 57, 32, 46, 4, 23, 80, 75, 22, 33], [41, 62, 38, 56, 63, 77, 85, 76, 55, 51, 90, 65, 57, 86, 27, 57, 55, 96, 72, 98, 82, 4, 65, 56, 53, 44, 16, 94, 23, 31, 28, 50, 16, 41, 9, 2, 43, 66, 96, 80, 77, 49, 91, 95, 97, 21, 19, 57, 77], [60, 19, 99, 64, 35, 33, 67, 85, 87, 48, 60, 45, 75, 68, 68, 15, 92, 72, 88, 98, 15, 23, 60, 91, 14, 2, 99, 43, 71, 16, 86, 28, 32, 71, 86, 2, 72, 7, 38, 48, 85, 86, 99, 82, 73, 2, 42, 42, 81], [20, 6, 11, 69, 74, 87, 97, 40, 36, 51, 47, 98, 17, 26, 53, 48, 27, 46, 67, 19, 72, 81, 65, 71, 36, 67, 83, 42, 91, 67, 98, 69, 49, 37, 46, 80, 56, 63, 78, 30, 96, 63, 76, 91, 26, 93, 23, 86, 20], [46, 80, 31, 67, 21, 51, 39, 63, 69, 20, 23, 96, 42, 73, 3, 27, 91, 74, 80, 24, 87, 9, 2, 6, 99, 71, 79, 21, 87, 29, 13, 69, 42, 1, 20, 43, 1, 99, 40, 7, 35, 52, 34, 50, 69, 29, 91, 71, 1], [73, 58, 65, 91, 17, 62, 96, 94, 79, 42, 28, 3, 92, 5, 66, 54, 38, 80, 44, 81, 76, 90, 57, 71, 24, 80, 82, 59, 8, 91, 90, 95, 82, 2, 41, 87, 56, 48, 22, 97, 18, 79, 41, 67, 48, 23, 2, 4, 26], [19, 49, 74, 86, 53, 6, 62, 1, 16, 52, 7, 88, 35, 78, 68, 15, 57, 23, 83, 78, 91, 86, 11, 4, 58, 96, 40, 58, 88, 98, 67, 38, 2, 87, 40, 84, 56, 72, 35, 49, 67, 96, 95, 44, 31, 65, 76, 18, 88], [36, 62, 29, 89, 23, 3, 30, 81, 45, 49, 94, 19, 64, 5, 56, 34, 73, 48, 26, 5, 88, 31, 24, 85, 22, 22, 85, 57, 30, 47, 74, 67, 39, 93, 89, 66, 77, 91, 29, 14, 4, 72, 5, 44, 91, 24, 98, 28, 24], [5, 13, 82, 55, 81, 30, 83, 86, 49, 82, 90, 15, 92, 30, 28, 84, 4, 68, 15, 34, 75, 87, 99, 43, 99, 75, 61, 63, 2, 52, 52, 15, 40, 28, 95, 96, 98, 55, 50, 22, 29, 72, 86, 12, 87, 38, 2, 12, 55], [85, 12, 95, 9, 79, 32, 73, 88, 8, 28, 56, 82, 36, 37, 32, 85, 39, 49, 93, 18, 23, 33, 73, 51, 43, 4, 80, 67, 72, 80, 2, 45, 83, 88, 80, 40, 2, 32, 1, 18, 64, 32, 9, 55, 67, 24, 11, 28, 16], [93, 12, 68, 90, 4, 75, 66, 31, 56, 50, 67, 89, 98, 1, 69, 39, 52, 95, 36, 67, 12, 61, 80, 72, 11, 14, 91, 82, 54, 8, 33, 4, 30, 84, 94, 91, 89, 54, 6, 5, 78, 51, 14, 34, 41, 89, 39, 18, 20], [8, 26, 85, 27, 32, 42, 50, 81, 49, 65, 63, 27, 75, 35, 38, 38, 42, 42, 49, 57, 54, 10, 60, 40, 1, 86, 64, 81, 12, 57, 77, 89, 26, 40, 43, 97, 72, 13, 90, 56, 17, 88, 24, 76, 95, 58, 80, 61, 80], [94, 28, 67, 97, 51, 88, 94, 92, 39, 66, 77, 74, 40, 13, 19, 6, 18, 9, 81, 68, 54, 50, 70, 11, 55, 42, 90, 11, 72, 67, 2, 82, 66, 26, 76, 37, 90, 36, 16, 78, 66, 21, 7, 11, 56, 44, 54, 93, 57], [58, 37, 48, 62, 39, 92, 64, 68, 68, 27, 70, 98, 82, 60, 44, 30, 97, 58, 84, 36, 5, 99, 19, 12, 90, 60, 83, 11, 53, 20, 73, 84, 27, 58, 5, 74, 9, 89, 77, 32, 72, 54, 45, 27, 86, 28, 18, 87, 31], [41, 34, 7, 5, 21, 6, 45, 35, 87, 3, 33, 38, 87, 80, 89, 16, 89, 71, 8, 3, 69, 19, 7, 86, 90, 50, 89, 6, 5, 61, 86, 95, 58, 22, 57, 75, 32, 17, 58, 41, 22, 80, 42, 79, 8, 46, 48, 3, 77], [30, 28, 73, 76, 25, 37, 85, 51, 39, 83, 72, 67, 86, 1, 38, 52, 63, 52, 83, 85, 60, 13, 91, 17, 84, 30, 38, 11, 27, 38, 28, 26, 33, 32, 54, 25, 24, 40, 27, 46, 86, 84, 97, 69, 93, 69, 39, 81, 29], [75, 86, 31, 65, 15, 83, 74, 9, 13, 45, 90, 6, 44, 2, 29, 48, 12, 87, 67, 50, 11, 5, 45, 74, 47, 6, 80, 95, 87, 94, 84, 89, 99, 69, 63, 67, 47, 34, 12, 27, 69, 86, 68, 28, 71, 45, 98, 2, 9], [79, 31, 36, 15, 97, 62, 31, 27, 2, 73, 43, 1, 83, 9, 60, 2, 58, 65, 12, 55, 90, 10, 65, 65, 61, 95, 75, 69, 35, 11, 68, 38, 39, 21, 36, 92, 72, 20, 43, 21, 35, 64, 32, 36, 69, 52, 4, 7, 98], [84, 71, 24, 21, 57, 73, 19, 84, 28, 32, 34, 16, 38, 81, 75, 4, 56, 40, 50, 40, 82, 49, 48, 6, 96, 5, 79, 45, 16, 17, 59, 56, 79, 35, 8, 99, 61, 27, 78, 87, 20, 57, 70, 88, 23, 76, 2, 27, 32], [93, 50, 64, 40, 33, 29, 33, 17, 74, 65, 43, 63, 81, 92, 58, 91, 43, 37, 46, 25, 98, 67, 93, 99, 51, 74, 38, 38, 1, 54, 65, 96, 22, 61, 58, 54, 19, 99, 70, 34, 79, 44, 67, 52, 22, 29, 14, 94, 62], [15, 93, 14, 67, 22, 97, 87, 7, 84, 7, 17, 32, 79, 77, 56, 62, 58, 58, 3, 89, 96, 80, 1, 67, 20, 92, 86, 62, 56, 53, 65, 56, 78, 45, 79, 96, 18, 48, 38, 22, 80, 75, 71, 73, 1, 42, 72, 75, 69], [29, 6, 56, 12, 39, 71, 12, 33, 83, 53, 19, 58, 85, 83, 43, 73, 45, 86, 19, 37, 11, 56, 25, 99, 69, 45, 62, 95, 14, 77, 34, 98, 82, 60, 64, 70, 51, 42, 21, 5, 66, 70, 61, 8, 66, 87, 62, 20, 4], [15, 94, 56, 20, 24, 9, 21, 41, 13, 5, 64, 46, 78, 71, 70, 59, 76, 51, 16, 51, 96, 42, 11, 68, 93, 52, 98, 73, 10, 72, 63, 36, 96, 45, 6, 6, 91, 66, 73, 64, 38, 69, 98, 61, 78, 74, 63, 71, 20]],34,),
    ([[64, 81, 37, 36, 97, 10, 34, 45, 63, 13, 25, 44, 97], [74, 24, 69, 74, 47, 91, 50, 36, 33, 92, 3, 31, 60], [29, 44, 45, 42, 21, 32, 28, 85, 47, 99, 94, 47, 17], [29, 48, 2, 33, 63, 68, 39, 89, 5, 68, 52, 52, 29], [37, 8, 20, 41, 70, 36, 32, 5, 20, 68, 22, 97, 31], [41, 93, 5, 10, 75, 37, 56, 86, 24, 85, 16, 2, 15], [41, 63, 49, 26, 94, 66, 29, 70, 60, 65, 40, 11, 52], [87, 90, 95, 79, 73, 64, 98, 81, 99, 3, 11, 28, 62], [48, 28, 46, 64, 55, 83, 2, 96, 75, 16, 11, 3, 55], [42, 29, 69, 92, 31, 77, 25, 6, 60, 67, 22, 41, 53], [60, 39, 55, 96, 30, 71, 89, 2, 8, 63, 59, 97, 28], [74, 38, 18, 62, 77, 85, 97, 23, 65, 40, 60, 85, 5], [99, 18, 38, 29, 26, 60, 36, 82, 29, 31, 63, 13, 94]],12,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if HalfDiagonalSums(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))