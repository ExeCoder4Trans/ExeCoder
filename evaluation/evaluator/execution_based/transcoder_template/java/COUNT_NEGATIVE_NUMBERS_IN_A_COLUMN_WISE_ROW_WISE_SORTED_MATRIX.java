// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;
import javafx.util.Pair;
public class COUNT_NEGATIVE_NUMBERS_IN_A_COLUMN_WISE_ROW_WISE_SORTED_MATRIX{
static int f_gold ( int M [ ] [ ] , int n , int m ) {
  int count = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    for ( int j = 0 ;
    j < m ;
    j ++ ) {
      if ( M [ i ] [ j ] < 0 ) count += 1 ;
      else break ;
    }
  }
  return count ;
}


//TOFILL

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ] [ ]> param0 = new ArrayList<>();
    param0.add(new int[][]{new int[]{31,92,57,28,79,84,92,19,31,71,91,46,60,79,82,4,70,82,41,79,80,29,26,76,92,18,94,55,46,69,67,60,85,25,11},new int[]{58,69,14,55,6,69,81,60,38,52,81,80,1,47,42,82,2,70,68,71,50,98,84,1,45,24,49,33,56,4,60,42,14,45,13},new int[]{28,92,91,71,75,97,30,9,76,94,55,84,76,38,32,7,73,49,37,76,41,3,89,56,71,99,71,25,94,37,43,9,89,55,55},new int[]{77,31,94,14,2,88,64,71,57,18,81,51,66,82,16,46,15,28,48,54,49,34,80,12,26,64,41,46,32,87,18,12,38,28,88},new int[]{84,93,86,10,92,89,62,65,33,66,92,52,28,49,98,37,49,91,42,64,43,12,83,61,51,11,80,35,28,50,35,1,31,81,77},new int[]{22,30,43,76,37,59,48,82,40,2,66,58,7,13,38,73,14,28,55,52,28,10,98,93,97,27,1,50,80,83,11,82,80,7,38},new int[]{54,30,50,31,57,2,73,56,24,35,85,99,28,51,83,86,82,30,72,98,40,81,15,5,18,76,62,5,50,37,99,46,31,16,66},new int[]{52,62,92,37,29,66,66,98,1,56,60,85,43,98,46,34,21,71,28,84,92,93,58,79,3,37,76,14,63,33,46,8,2,56,31},new int[]{70,69,43,26,58,80,60,28,24,79,42,80,16,52,17,93,25,16,77,35,39,16,77,19,45,27,96,44,30,88,76,6,18,2,33},new int[]{1,6,28,49,25,25,14,31,5,60,78,45,20,88,9,80,72,46,75,90,26,11,25,77,22,39,83,65,95,64,78,86,23,48,20},new int[]{98,5,39,62,57,87,52,68,32,98,90,99,67,81,94,96,15,44,13,17,47,35,84,14,23,69,5,96,42,42,65,60,10,10,88},new int[]{4,91,15,32,39,40,39,26,25,26,35,22,5,46,72,27,44,23,49,67,9,17,64,74,68,84,94,76,22,22,30,29,26,63,51},new int[]{10,53,32,7,39,74,91,85,79,47,47,11,54,51,43,75,19,74,33,27,15,29,96,96,87,83,62,32,79,62,43,62,97,87,16},new int[]{11,15,6,98,56,59,40,13,99,53,48,46,99,16,59,58,21,57,89,63,67,50,71,98,10,49,78,39,5,64,9,7,60,86,83},new int[]{94,9,64,64,80,70,1,77,15,64,69,43,40,56,82,28,15,92,40,38,61,74,32,1,95,30,5,43,1,8,57,5,5,97,54},new int[]{79,58,95,22,97,60,97,87,35,14,58,59,86,89,57,33,1,71,16,48,77,69,6,99,74,96,79,98,65,86,32,45,61,49,36},new int[]{19,37,45,27,48,21,83,82,96,85,83,54,37,22,38,43,45,28,84,91,38,16,58,46,48,20,61,8,90,66,42,47,65,60,15},new int[]{48,19,73,34,64,86,86,4,50,81,67,14,28,49,83,56,97,24,38,84,39,82,1,14,7,32,90,7,7,47,85,55,96,87,83},new int[]{70,68,59,18,72,95,7,62,53,22,82,64,72,3,24,52,26,41,30,19,47,55,13,10,69,54,93,42,44,49,72,18,29,70,85},new int[]{96,40,94,49,87,60,26,23,86,18,72,90,32,11,48,47,94,96,98,59,11,19,27,49,62,29,23,22,1,88,54,41,39,76,44},new int[]{45,99,44,67,5,80,36,33,89,52,2,49,74,36,7,14,57,67,62,97,22,92,44,2,65,67,58,91,56,84,53,49,11,13,24},new int[]{69,81,60,52,34,72,33,56,28,17,3,62,7,78,40,19,95,42,49,77,90,42,22,1,60,92,65,28,11,83,19,59,52,45,26},new int[]{23,17,21,54,31,32,81,15,13,65,62,16,21,70,6,84,5,91,37,20,89,73,3,65,86,24,27,11,98,92,54,23,9,1,90},new int[]{53,67,14,42,52,55,52,86,99,43,74,48,71,55,85,87,73,41,55,52,83,67,78,14,15,27,83,28,65,35,45,33,59,13,34},new int[]{29,4,17,82,11,18,95,71,10,34,79,43,45,58,9,26,84,9,49,6,63,41,43,75,35,54,55,18,81,55,2,53,1,67,87},new int[]{98,3,18,56,33,97,20,90,38,80,83,80,18,94,11,43,60,85,30,2,89,85,32,35,62,32,93,71,62,93,24,33,86,21,32},new int[]{38,45,16,40,18,67,71,49,46,98,64,83,35,78,40,86,28,66,77,24,31,10,82,1,31,9,47,39,84,51,1,6,32,4,63},new int[]{85,48,64,11,29,77,59,1,99,17,17,38,49,78,82,50,87,75,18,75,73,98,17,27,51,4,98,96,6,74,5,47,52,47,75},new int[]{36,68,16,99,38,84,45,71,71,36,3,97,69,15,48,77,6,4,33,36,67,65,52,55,37,35,76,69,98,84,62,5,80,15,36},new int[]{67,84,38,44,5,66,58,57,67,75,61,66,60,2,66,50,6,83,91,86,67,99,1,32,71,91,52,29,51,73,23,32,4,75,25},new int[]{24,94,50,60,28,73,99,1,10,37,54,96,56,46,19,9,57,78,19,70,76,25,14,87,13,22,63,73,97,3,19,39,16,36,22},new int[]{92,41,48,68,30,72,1,76,98,58,57,61,32,11,58,29,80,86,22,94,50,66,78,22,91,56,91,82,61,67,12,18,46,99,69},new int[]{49,64,35,55,67,78,11,71,12,98,10,9,82,35,61,40,29,10,83,11,63,16,97,97,96,91,30,97,21,91,32,61,27,33,35},new int[]{29,58,88,23,96,94,1,55,79,30,87,83,5,70,25,62,14,67,29,22,84,2,25,75,11,57,89,65,80,82,36,28,45,44,4},new int[]{70,94,49,13,26,24,42,24,58,83,41,6,50,78,22,12,21,84,70,28,44,51,78,75,9,70,37,23,60,25,68,97,49,17,27}});
    param0.add(new int[][]{new int[]{22,49,27,1,69,48,44,18,89,36,93,10,67,18,7,62,55,3,84,76,49,57},new int[]{59,6,37,2,33,16,20,60,69,98,92,2,70,12,99,57,32,92,64,92,68,62},new int[]{41,89,70,69,62,88,52,23,8,37,77,87,54,44,87,32,53,29,38,80,68,32},new int[]{63,77,82,97,7,56,2,68,44,52,40,8,71,50,26,62,18,61,12,20,1,76},new int[]{44,47,86,67,53,27,80,57,53,74,7,11,86,58,7,55,30,57,23,97,38,33},new int[]{48,84,9,77,60,53,41,15,99,30,90,36,89,64,78,63,51,51,22,17,72,50},new int[]{14,56,77,30,59,64,26,22,86,92,80,88,63,46,81,3,81,64,14,72,14,77},new int[]{36,48,97,59,34,64,11,24,41,30,37,66,33,98,60,27,76,90,48,10,90,41},new int[]{76,54,4,86,40,31,85,51,38,72,28,12,35,99,78,12,13,49,34,33,21,83},new int[]{37,15,61,52,17,81,90,44,16,13,2,92,88,84,18,99,10,71,82,33,75,44},new int[]{40,49,88,11,67,52,39,2,92,49,52,31,77,97,51,31,66,98,66,37,25,62},new int[]{99,9,6,66,15,61,15,58,33,62,80,65,59,1,79,54,78,51,97,19,83,59},new int[]{3,76,87,47,71,66,86,18,79,62,44,67,5,82,94,27,48,2,88,34,55,46},new int[]{38,66,48,93,40,7,6,14,82,56,83,2,8,58,21,26,90,10,85,3,8,78},new int[]{54,43,93,86,42,41,87,70,67,60,90,78,66,42,30,57,76,2,30,24,12,49},new int[]{12,5,75,55,17,62,87,21,91,88,10,20,49,46,79,51,33,94,59,48,97,70},new int[]{49,75,21,53,2,92,14,80,92,40,84,67,39,48,53,49,68,57,14,58,97,9},new int[]{45,23,2,43,89,62,28,46,74,38,70,84,67,22,62,86,72,24,39,5,64,43},new int[]{28,93,44,61,47,23,52,97,62,31,98,1,63,7,86,46,66,61,24,14,15,62},new int[]{60,58,17,60,19,91,78,22,56,84,99,91,42,55,30,83,84,42,86,73,76,53},new int[]{95,93,92,53,56,72,31,67,4,61,39,88,64,94,48,88,23,54,37,10,18,67},new int[]{97,70,9,43,34,94,43,71,13,81,56,73,85,54,35,89,45,18,8,54,70,36}});
    param0.add(new int[][]{new int[]{54,62,19,8,61,82,54,69,91,14,56,78,22,81,38,47},new int[]{22,25,33,85,89,78,7,42,24,24,24,74,89,83,23,1},new int[]{79,9,51,67,71,49,87,45,81,2,4,50,16,71,91,44},new int[]{77,99,85,40,90,45,3,54,39,69,40,88,81,41,84,24},new int[]{84,24,42,18,51,45,16,97,97,64,56,35,9,33,37,97},new int[]{61,55,53,21,5,1,71,23,87,71,59,83,27,77,9,9},new int[]{60,42,94,10,69,95,98,38,54,64,17,71,83,38,60,38},new int[]{2,45,33,60,92,31,55,48,31,19,79,9,81,47,4,38},new int[]{68,16,10,37,43,45,10,93,47,99,74,88,79,85,2,27},new int[]{69,72,66,74,32,60,90,70,88,68,15,72,65,35,87,75},new int[]{49,36,73,88,81,8,78,65,98,35,5,5,46,53,39,92},new int[]{5,39,16,95,34,59,36,19,80,5,69,39,26,45,15,11},new int[]{14,95,52,74,90,61,75,19,71,69,37,45,8,71,49,26},new int[]{71,95,22,95,95,48,53,75,96,68,82,99,9,15,4,54},new int[]{26,94,94,81,47,4,22,74,41,98,98,11,89,77,7,65},new int[]{47,37,49,52,68,83,51,70,32,47,60,93,61,10,21,42}});
    param0.add(new int[][]{new int[]{39,79,41,68,91,31,87,47,16,92,42,68,79,59,17,45,68,78,99,19,51},new int[]{43,46,81,76,18,20,62,54,42,52,8,66,3,79,60,12,50,87,88,70,11},new int[]{49,2,91,98,51,74,47,72,32,42,92,52,98,89,9,91,86,38,78,89,42},new int[]{45,76,87,45,3,88,56,16,16,59,78,40,9,7,55,69,58,39,64,2,32},new int[]{65,45,40,81,13,71,33,46,27,47,92,5,9,75,80,2,90,50,40,4,1},new int[]{99,5,44,17,65,99,27,27,5,1,87,95,78,27,4,40,57,79,82,46,33},new int[]{99,3,6,49,52,24,66,91,66,84,92,96,48,24,81,69,46,58,16,49,83},new int[]{2,42,95,3,17,63,45,82,69,10,86,44,64,55,2,44,93,16,98,3,41},new int[]{27,2,95,31,58,64,21,14,90,14,86,42,84,47,4,82,70,47,97,1,49},new int[]{59,74,19,7,3,89,77,72,52,57,86,31,70,55,89,25,43,52,24,50,30},new int[]{89,57,9,45,89,74,76,89,23,90,57,77,38,25,49,3,85,90,90,26,47},new int[]{55,39,1,53,31,10,76,47,77,33,6,22,29,95,29,14,32,28,27,11,93},new int[]{95,75,56,23,21,30,76,98,25,79,41,3,63,87,96,53,92,40,74,22,8},new int[]{91,35,88,59,74,92,5,6,56,42,97,80,14,45,12,61,63,79,73,52,81},new int[]{73,86,4,14,11,1,47,35,12,99,37,31,61,86,60,17,28,82,3,18,20},new int[]{46,85,58,67,3,32,53,13,86,7,78,12,29,48,58,37,77,43,75,14,42},new int[]{38,93,44,22,94,76,29,63,20,19,51,57,53,11,9,63,24,43,51,11,37},new int[]{19,71,53,61,91,91,20,99,7,81,88,37,29,9,23,10,22,38,55,89,29},new int[]{62,33,81,98,9,79,80,50,63,67,64,95,69,84,22,4,98,71,1,81,77},new int[]{97,1,28,52,20,16,45,31,69,9,98,60,55,97,5,3,95,77,65,54,32},new int[]{71,97,30,68,74,7,15,99,62,39,20,55,30,22,20,31,54,31,93,10,80}});
    param0.add(new int[][]{new int[]{48,19,66,15,8,54,8,66,22,72,93,33,96,26,89,57,86,16,99,75,9,20,36,26},new int[]{67,60,72,35,68,26,18,53,54,82,23,15,89,43,82,1,33,46,61,87,93,27,33,21},new int[]{7,78,68,44,49,95,1,16,16,7,1,92,3,44,47,52,31,61,41,28,95,28,51,46},new int[]{98,90,93,45,10,2,88,20,1,67,2,75,27,31,68,59,11,50,4,40,5,61,34,24},new int[]{41,37,20,59,32,13,84,27,58,17,40,54,43,7,30,97,90,6,40,68,95,99,2,81},new int[]{83,50,27,89,94,39,35,9,45,45,9,20,25,12,36,18,74,75,69,66,37,82,16,25},new int[]{84,20,8,12,15,79,41,13,81,39,48,76,65,89,70,85,93,48,51,16,87,37,30,96},new int[]{29,45,15,54,15,54,4,36,9,81,22,74,25,17,61,80,78,70,39,46,14,16,69,43},new int[]{32,81,24,3,19,56,37,2,42,2,87,90,14,41,50,66,5,32,83,72,62,16,87,46},new int[]{17,7,38,46,97,72,9,17,32,80,47,15,20,21,61,28,11,12,34,86,11,50,98,66},new int[]{32,52,6,16,31,72,58,64,21,10,33,37,34,32,34,21,44,82,82,66,70,99,50,6},new int[]{90,84,81,74,86,24,34,66,16,89,58,92,98,12,71,74,6,9,35,41,32,78,1,42},new int[]{1,24,27,69,79,52,11,85,7,66,11,24,90,72,98,15,37,33,36,68,16,69,66,62},new int[]{25,97,59,93,94,2,46,61,60,24,19,21,7,91,93,19,1,84,70,46,19,36,44,31},new int[]{97,67,2,88,1,15,75,35,48,69,72,53,90,75,74,59,8,53,39,29,4,44,92,24},new int[]{87,84,38,81,81,71,32,87,72,23,34,6,88,33,56,25,31,28,89,50,14,55,1,7},new int[]{85,64,80,66,71,99,62,53,87,71,86,59,74,85,68,31,38,34,36,14,13,95,81,47},new int[]{25,70,61,78,68,26,23,57,84,61,14,22,40,83,68,29,75,21,54,92,47,29,47,64},new int[]{43,12,8,16,12,80,76,31,22,96,74,64,30,54,39,60,13,8,44,80,56,45,58,28},new int[]{54,12,30,68,79,24,78,79,64,33,40,44,74,50,31,94,44,42,57,4,82,66,27,77},new int[]{80,2,92,92,97,18,55,73,34,26,1,11,3,3,51,13,49,65,70,8,33,88,93,97},new int[]{34,96,94,8,28,58,22,8,60,57,86,16,84,63,21,84,59,83,75,46,95,54,52,16},new int[]{81,18,98,77,20,14,13,18,2,86,46,48,49,26,69,54,63,76,97,11,39,58,75,87},new int[]{36,48,94,97,96,39,34,90,17,48,72,39,85,40,63,85,41,55,23,76,39,21,52,27}});
    param0.add(new int[][]{new int[]{45,42,10,70,41,89,22,51,39,46,25,16,53,79,40,94,32,42,36,72,38,23,87,9,24},new int[]{76,21,4,75,31,69,97,57,38,25,98,78,51,37,19,29,73,57,81,83,82,19,25,93,80},new int[]{72,9,91,68,96,53,68,30,52,70,80,60,61,53,25,30,10,36,92,15,19,75,83,54,57},new int[]{6,31,21,12,97,20,53,80,76,41,42,1,9,89,35,3,68,29,20,29,18,86,67,21,83},new int[]{45,46,53,3,55,32,40,51,40,54,89,93,81,5,93,28,7,19,84,62,21,53,55,16,25},new int[]{55,37,70,58,26,71,89,81,11,29,66,99,82,2,86,91,47,90,30,45,70,62,10,13,77},new int[]{48,68,68,43,69,27,80,39,88,28,70,36,19,79,86,11,53,74,99,77,37,88,97,66,7},new int[]{58,69,76,76,50,29,40,47,2,67,12,42,27,27,57,48,77,49,93,24,83,27,81,1,58},new int[]{78,82,51,58,67,53,97,94,77,33,98,18,66,87,96,50,77,8,62,21,71,87,83,56,54},new int[]{95,45,29,19,52,65,12,58,38,50,80,27,80,31,66,35,68,51,47,96,62,94,22,66,21},new int[]{23,29,38,27,67,30,52,15,90,85,25,67,51,91,92,71,81,17,79,50,23,80,29,64,74},new int[]{7,79,94,85,6,82,98,69,37,93,82,93,76,94,87,93,84,7,67,18,27,70,98,25,62},new int[]{64,31,65,86,15,8,13,23,35,54,57,62,45,50,20,81,58,34,69,35,94,13,44,78,48},new int[]{98,25,26,89,53,89,20,20,51,54,76,28,55,45,75,86,90,29,41,19,1,63,17,51,5},new int[]{26,68,55,36,33,15,92,63,9,53,97,63,9,63,95,8,28,74,58,57,35,66,56,17,40},new int[]{40,73,83,78,5,28,71,97,66,84,47,47,13,92,99,71,15,17,86,19,74,33,17,63,20},new int[]{59,14,65,17,39,59,61,95,62,32,33,39,88,49,87,11,17,32,19,11,61,95,75,50,5},new int[]{81,34,42,39,28,11,20,98,60,26,2,8,64,10,55,94,24,66,88,13,81,37,99,83,83},new int[]{92,18,41,52,83,78,53,87,26,47,14,97,91,45,77,37,39,22,1,46,52,42,8,99,17},new int[]{30,40,15,66,32,80,35,5,90,6,56,30,51,33,48,74,9,51,58,46,32,47,59,97,33},new int[]{60,14,19,5,98,49,4,94,66,59,44,28,35,60,12,80,80,6,42,99,7,35,72,76,60},new int[]{73,83,80,67,93,71,52,2,91,88,30,12,70,74,88,4,21,65,12,79,48,25,8,85,82},new int[]{20,75,62,20,10,71,60,52,34,17,58,88,64,3,37,52,35,20,9,20,80,36,15,94,88},new int[]{19,47,94,21,5,37,13,40,74,87,17,48,9,65,96,33,68,25,72,43,85,50,70,82,80},new int[]{21,88,58,48,84,38,37,33,92,56,16,71,9,50,45,66,61,61,93,37,97,36,38,3,2}});
    param0.add(new int[][]{new int[]{67,61,32,22,31,43,25,63,3,92,10,14,64,23,61,58,67,98,19,25,98,71,41,23,17,63,20,17,59,89,92,20,28,94,38,41,20,63,67,88,68,90,50,64},new int[]{64,48,46,95,50,42,25,50,77,30,3,62,81,31,11,99,52,24,70,86,98,27,53,71,24,84,1,34,70,51,75,57,37,14,83,21,82,88,4,56,88,66,31,88},new int[]{48,68,58,58,7,23,44,49,84,87,89,22,42,4,57,60,36,54,69,3,61,82,14,41,37,69,76,30,78,74,93,79,82,44,6,66,37,80,98,20,32,13,99,73},new int[]{58,86,91,80,4,35,46,27,79,87,94,34,24,22,21,94,16,72,91,70,53,66,64,42,71,31,36,77,70,65,39,22,43,41,23,85,20,32,77,9,16,11,88,71},new int[]{6,33,85,2,73,8,3,3,48,45,21,63,77,46,71,47,54,93,40,56,95,77,13,51,43,58,18,26,96,63,62,69,60,72,47,74,44,77,17,9,7,69,5,90},new int[]{25,49,72,10,59,4,11,43,79,15,66,50,59,42,72,57,13,65,74,93,90,52,34,26,12,43,34,6,63,27,47,45,4,96,51,21,74,91,12,21,34,94,55,75},new int[]{72,45,43,54,9,93,57,13,59,90,47,16,78,82,98,94,7,98,40,70,57,83,42,6,36,60,96,11,38,36,79,5,24,84,35,70,61,3,54,64,58,65,54,80},new int[]{91,61,97,86,81,18,9,66,58,55,73,86,13,95,10,49,12,98,97,85,47,37,67,62,12,25,51,69,77,47,91,66,85,74,69,10,96,66,41,30,95,43,66,31},new int[]{57,50,96,40,96,8,25,10,88,47,54,54,55,72,77,60,97,87,5,30,24,1,96,95,81,89,42,65,69,34,88,37,4,48,10,74,44,55,84,76,72,17,97,38},new int[]{93,52,95,81,54,74,7,40,98,99,79,39,14,58,72,9,66,11,67,77,74,83,75,31,82,67,80,80,18,26,84,61,36,3,13,22,16,87,55,13,42,19,95,3},new int[]{83,10,52,84,97,72,53,18,85,10,1,53,96,7,57,14,27,77,15,86,12,46,59,23,30,58,63,68,19,94,4,57,25,33,17,97,88,80,10,24,13,55,71,6},new int[]{97,7,58,88,38,52,32,12,93,50,58,97,24,85,77,91,52,10,56,18,61,85,58,7,7,64,22,81,94,60,42,68,84,76,83,50,28,82,89,27,96,43,28,39},new int[]{86,3,88,2,33,97,8,15,40,94,84,9,62,6,39,47,9,10,29,6,52,78,87,4,64,20,85,7,89,8,50,83,4,49,72,44,24,49,21,72,64,84,39,51},new int[]{88,80,76,94,47,13,29,30,85,20,85,92,78,2,59,7,87,24,86,83,25,8,26,22,93,56,74,19,9,7,71,65,79,25,76,63,87,93,44,16,76,92,98,85},new int[]{67,42,81,11,30,32,64,67,30,8,22,70,35,47,5,35,89,82,31,98,42,50,87,99,18,24,35,81,40,11,83,52,16,69,53,97,73,16,37,2,32,60,86,89},new int[]{39,47,27,27,81,67,65,76,8,75,27,21,44,48,61,94,42,22,46,15,95,97,57,9,61,78,74,13,48,48,89,91,37,2,8,85,19,56,27,22,26,19,49,94},new int[]{87,67,37,46,62,40,85,22,73,99,51,36,99,47,43,13,37,91,58,71,90,93,73,15,92,84,1,59,3,84,36,66,8,23,16,88,79,43,52,10,15,69,24,23},new int[]{19,47,92,46,24,53,91,58,15,30,46,82,43,65,88,68,18,90,24,35,41,69,48,53,48,86,65,75,2,87,89,40,26,3,95,2,24,32,37,57,85,94,77,81},new int[]{24,26,2,36,32,10,44,77,59,11,15,98,12,47,70,44,18,7,6,16,67,23,3,51,51,82,86,6,18,53,49,25,22,42,99,83,90,85,66,22,22,26,15,24},new int[]{84,24,11,3,88,47,6,60,25,92,84,11,42,25,81,18,81,43,8,85,79,27,99,5,16,66,79,14,73,78,29,74,15,95,13,79,39,36,79,60,6,85,36,81},new int[]{6,20,9,7,85,83,50,31,90,91,7,38,20,26,15,14,53,49,7,9,15,17,94,18,88,63,22,34,26,66,54,30,9,19,53,11,13,5,32,51,35,48,82,63},new int[]{80,96,47,59,1,91,84,75,95,31,43,32,70,34,95,54,13,49,27,73,50,69,29,75,17,50,88,42,76,95,51,19,87,34,91,20,90,5,64,2,34,54,76,46},new int[]{85,70,55,7,39,24,41,60,89,74,2,18,50,75,96,84,1,97,18,1,42,23,17,59,98,44,49,83,50,50,77,37,12,56,32,67,72,6,32,65,7,76,52,54},new int[]{46,45,14,49,65,22,4,3,28,21,43,19,1,35,31,50,67,46,65,44,74,3,76,27,84,74,66,97,14,21,32,93,45,27,57,51,9,72,27,50,44,45,11,69},new int[]{25,24,88,33,90,89,56,49,69,69,2,85,95,78,79,51,46,26,20,99,3,99,2,27,82,59,24,57,68,94,17,26,10,19,86,24,50,44,28,5,69,23,68,9},new int[]{29,5,31,57,47,89,65,37,32,54,64,70,48,19,50,88,88,84,33,84,1,42,43,83,90,64,72,8,58,80,33,96,4,53,84,58,29,70,24,96,36,37,58,97},new int[]{73,47,38,22,77,37,38,22,3,57,14,27,59,24,68,68,87,94,5,32,97,26,52,90,46,65,69,14,33,66,63,70,57,80,82,89,77,15,79,91,75,67,4,53},new int[]{88,3,45,71,71,2,27,68,22,59,58,47,89,82,74,10,32,24,74,68,36,20,98,83,34,6,75,36,26,7,74,98,19,61,86,16,86,51,46,46,81,59,39,79},new int[]{84,11,50,52,59,41,98,62,3,23,91,15,83,4,37,36,77,97,66,19,37,92,79,32,18,50,53,1,71,28,95,7,12,11,80,78,81,11,98,92,28,5,23,49},new int[]{37,57,14,93,49,66,35,63,83,84,19,20,17,16,83,21,28,29,7,10,70,55,54,24,86,85,8,83,27,87,63,46,45,39,8,18,78,75,6,2,67,33,2,58},new int[]{9,52,26,95,57,4,49,80,60,90,39,83,14,49,22,99,7,72,62,11,76,99,33,93,90,53,20,47,23,89,5,22,16,89,40,89,54,22,74,51,11,21,79,80},new int[]{66,12,85,75,41,2,23,46,57,90,45,32,77,74,90,73,75,22,3,13,94,89,2,12,64,4,45,21,35,45,33,44,86,86,44,40,97,51,30,46,76,20,76,5},new int[]{35,15,99,54,22,51,23,42,37,47,90,34,11,50,32,78,42,54,28,28,36,5,51,45,44,47,83,48,5,38,98,73,97,72,81,45,40,94,51,1,35,63,69,48},new int[]{53,69,64,24,50,8,77,80,54,15,52,5,17,55,80,35,7,80,14,91,34,30,61,99,59,39,32,18,39,1,26,75,2,8,46,63,24,99,97,23,86,58,77,61},new int[]{79,15,11,8,31,31,21,37,12,64,24,38,23,39,91,48,23,67,55,62,56,10,62,3,96,60,54,42,63,18,5,74,32,19,49,7,47,13,9,66,50,89,49,17},new int[]{9,14,44,11,27,85,41,71,76,60,29,15,82,35,91,54,31,26,34,47,8,46,85,99,61,50,15,25,66,7,16,69,11,72,90,17,6,94,12,34,47,62,88,96},new int[]{7,41,81,66,10,11,72,78,94,4,11,45,73,25,88,38,25,50,2,14,98,86,3,84,7,84,29,7,7,97,15,23,70,10,19,14,25,96,64,64,33,8,15,97},new int[]{31,90,82,65,98,19,90,90,7,1,20,19,39,39,56,30,94,65,43,74,12,89,81,28,16,88,54,74,31,91,44,52,80,13,95,62,10,10,79,91,71,31,66,92},new int[]{87,2,17,28,71,7,17,37,37,72,2,25,25,35,64,95,66,69,90,63,34,16,80,77,41,78,25,9,99,3,62,17,2,79,16,82,83,67,97,49,76,32,25,32},new int[]{22,53,6,71,49,38,44,43,77,95,28,19,76,12,82,48,91,25,66,50,78,28,44,69,26,83,25,15,96,20,77,1,33,88,8,38,28,79,34,34,29,78,9,52},new int[]{44,10,43,22,19,24,34,3,14,37,37,30,87,48,75,99,84,99,18,65,52,93,64,90,73,91,11,23,40,72,7,61,98,11,8,42,32,86,40,21,19,90,95,52},new int[]{12,51,98,82,51,4,86,40,74,1,82,26,56,54,89,81,38,73,25,18,3,95,8,86,38,6,55,56,65,40,88,40,68,41,84,40,93,7,16,79,5,52,20,71},new int[]{56,34,12,72,32,49,62,57,25,69,16,51,76,23,40,41,15,39,77,63,63,22,95,86,73,26,28,44,35,92,42,52,7,23,71,88,92,99,44,4,81,78,51,69},new int[]{29,17,82,37,10,15,25,54,37,30,60,73,16,85,56,98,42,99,14,46,78,50,72,61,72,4,39,99,71,55,50,46,80,21,96,49,47,10,70,29,60,16,24,60}});
    param0.add(new int[][]{new int[]{10,67,53,58,73,24,62,89,36,84,54,60,46,96,96,92,26,82,97,63},new int[]{48,41,1,86,53,43,18,90,36,96,15,29,95,85,70,25,86,25,26,76},new int[]{62,70,29,37,26,52,66,37,64,30,55,90,77,26,1,91,73,37,75,10},new int[]{37,25,56,27,77,68,12,12,31,9,54,8,6,38,8,59,80,17,35,10},new int[]{84,63,29,21,63,58,6,76,14,43,20,88,95,82,81,30,36,53,41,35},new int[]{12,20,52,81,63,57,16,97,91,89,19,62,95,56,54,13,6,61,67,86},new int[]{88,77,55,5,57,19,14,94,46,2,65,49,64,86,45,54,89,67,3,90},new int[]{46,18,40,16,53,95,61,90,34,18,86,6,99,4,42,20,33,87,51,81},new int[]{91,94,23,19,60,94,94,16,43,45,94,78,23,79,86,82,70,15,79,60},new int[]{43,54,93,45,56,71,75,98,99,22,35,76,48,98,67,29,12,97,37,77},new int[]{33,63,58,43,8,94,28,18,4,11,80,38,35,67,48,41,4,21,62,17},new int[]{48,23,50,36,84,41,78,91,78,38,72,52,41,21,14,53,32,43,1,65},new int[]{22,5,5,11,55,80,64,98,49,41,77,61,75,48,65,51,4,2,54,55},new int[]{36,33,97,47,39,18,23,11,93,47,58,76,33,76,18,21,22,53,87,72},new int[]{77,9,31,43,61,78,92,74,94,66,63,54,94,39,5,91,5,36,7,87},new int[]{10,50,16,13,94,93,26,48,80,23,56,93,85,46,16,37,73,86,50,41},new int[]{1,49,47,8,53,12,8,62,90,60,29,61,87,81,87,76,59,44,72,79},new int[]{9,63,35,78,26,57,4,37,95,93,13,52,40,76,28,9,94,80,76,96},new int[]{48,39,62,36,11,9,59,79,23,73,62,64,5,77,9,1,51,66,91,53},new int[]{38,84,93,19,79,34,77,87,14,83,86,10,36,65,98,5,78,15,66,87}});
    param0.add(new int[][]{new int[]{77,56,21,16,3,4,66,99,72,94,34,33,76,11,85,89,9,74},new int[]{19,31,23,11,31,52,97,53,56,6,28,4,68,74,92,14,90,64},new int[]{61,79,82,4,63,17,35,22,53,84,18,49,57,77,67,52,63,50},new int[]{15,14,6,59,1,21,5,46,43,70,54,51,90,94,92,97,91,53},new int[]{91,42,70,95,16,16,29,89,52,60,1,60,39,54,48,71,94,69},new int[]{4,86,36,45,15,74,86,35,5,55,14,51,81,76,76,67,32,1},new int[]{79,1,94,83,6,91,26,32,55,77,17,90,37,99,68,40,44,87},new int[]{63,57,15,2,26,35,92,15,16,53,14,4,49,99,18,47,35,85},new int[]{72,52,11,94,54,45,98,39,94,4,68,72,6,18,94,33,61,22},new int[]{20,62,47,73,41,88,83,88,96,73,4,67,28,91,11,56,95,15},new int[]{32,29,44,46,61,48,51,64,59,47,49,17,30,75,30,10,58,76},new int[]{96,46,69,13,88,44,82,58,93,96,43,51,91,86,68,72,6,83},new int[]{84,40,99,55,58,57,32,5,30,83,30,27,50,42,56,11,18,88},new int[]{3,94,46,14,38,91,36,62,80,54,62,60,83,93,97,4,38,36},new int[]{70,84,86,57,43,23,7,59,5,24,12,37,49,10,82,83,45,71},new int[]{25,75,55,79,31,96,47,61,25,1,66,12,16,46,84,52,57,50},new int[]{86,98,54,8,35,6,85,99,58,48,49,76,29,36,82,77,72,68},new int[]{95,53,87,51,41,30,56,16,31,33,48,91,17,90,47,59,75,7}});
    param0.add(new int[][]{new int[]{34,1,55,60,18,68,91,6,94,26,74,59,4,58,39,76,49,81,16,6,76,4,89,24,75,14,42,58,50,97,13,37,17,12,49,87,66,41,35,8,92,76,97,76,87,34,31,98},new int[]{90,60,31,75,59,62,78,99,32,64,98,14,13,54,62,66,71,90,8,14,79,19,22,89,55,57,14,64,90,48,26,49,5,1,92,2,25,59,49,62,56,24,79,60,70,18,93,11},new int[]{27,45,53,94,75,27,40,42,87,55,73,75,86,13,77,16,41,8,30,71,34,11,70,90,59,4,86,38,9,17,5,44,39,49,47,16,80,5,84,77,73,65,33,67,90,10,6,91},new int[]{86,24,6,58,22,53,14,6,38,5,94,58,77,96,52,88,57,76,19,80,52,61,41,25,6,42,34,25,77,58,12,1,45,42,67,9,8,53,79,53,54,34,69,21,68,49,86,9},new int[]{71,11,83,90,39,31,56,64,69,40,91,57,59,4,97,70,27,33,85,21,17,82,10,16,12,99,89,82,34,40,70,53,88,77,18,15,99,93,62,25,3,98,9,43,46,16,16,88},new int[]{43,71,10,81,76,35,37,17,59,7,86,34,53,27,4,49,61,89,73,14,38,7,63,73,8,78,29,28,62,72,25,54,89,86,99,15,59,29,57,67,67,18,72,85,51,76,69,43},new int[]{19,57,50,26,95,65,89,97,97,20,48,74,57,29,79,66,4,42,67,73,55,90,58,46,34,44,78,6,28,68,61,76,22,1,25,9,81,17,79,54,83,80,43,39,13,31,75,52},new int[]{46,21,43,57,20,54,26,30,88,15,65,17,37,49,52,84,81,57,72,89,46,79,89,42,20,8,76,45,34,18,90,24,36,70,80,18,22,58,93,92,95,72,95,46,36,65,5,16},new int[]{7,96,69,10,42,76,23,25,73,93,61,72,85,70,34,77,36,83,88,75,23,33,71,63,69,60,54,89,68,56,30,47,99,22,17,95,68,42,67,96,39,90,3,71,75,5,19,43},new int[]{23,91,35,60,60,78,49,80,78,42,86,42,3,2,7,45,57,84,49,35,91,16,39,51,34,1,99,57,36,18,34,44,62,84,41,15,78,78,46,33,39,2,75,79,7,90,99,34},new int[]{70,61,64,66,92,86,11,85,26,99,11,10,32,72,3,52,21,2,52,25,17,69,22,9,97,65,79,90,93,46,84,33,33,84,3,52,70,18,15,3,90,70,7,77,78,90,41,95},new int[]{20,62,11,12,16,66,64,45,10,33,79,52,34,17,57,47,24,37,57,89,74,63,38,59,50,90,27,60,63,72,89,24,76,42,82,30,69,30,22,49,83,29,26,70,57,48,54,40},new int[]{81,50,53,62,11,44,96,77,7,23,22,15,77,77,46,22,86,98,62,44,30,3,55,64,92,18,22,78,1,64,39,45,25,91,23,92,37,47,66,54,43,68,4,61,21,21,3,73},new int[]{94,88,19,88,94,42,38,60,83,36,92,52,72,89,53,52,25,28,49,77,42,75,80,46,15,80,40,51,58,89,4,19,54,66,39,40,12,13,5,92,86,37,85,72,6,60,55,36},new int[]{18,28,83,83,52,63,61,28,18,14,98,53,76,8,4,98,33,29,61,12,29,99,51,31,1,74,14,37,22,77,69,41,77,87,8,46,25,20,60,8,54,69,88,52,70,89,45,69},new int[]{98,51,93,91,42,33,87,62,1,31,5,12,37,87,29,40,59,11,1,46,78,82,90,6,23,98,90,79,36,87,83,25,61,89,11,63,3,11,96,98,23,81,62,83,79,4,43,54},new int[]{61,26,32,69,69,62,95,36,41,46,32,98,62,43,49,22,33,88,36,29,15,9,30,74,96,77,41,13,86,43,96,50,91,46,29,26,84,89,49,52,10,27,8,57,55,36,54,82},new int[]{89,6,53,46,51,50,49,69,7,38,53,96,84,23,13,62,40,35,12,41,38,72,72,40,83,57,2,58,18,42,20,51,71,11,71,93,53,16,35,17,8,99,57,39,99,14,22,7},new int[]{98,11,25,47,36,80,96,77,93,84,52,25,14,19,13,98,75,70,94,27,87,53,8,31,1,41,31,75,51,36,69,43,2,12,19,77,7,89,61,96,99,5,10,99,78,67,98,94},new int[]{61,48,23,56,86,87,32,87,39,93,86,41,48,32,8,80,31,54,77,48,8,28,31,73,48,84,32,4,45,7,19,34,91,36,13,9,50,83,9,50,90,79,78,15,37,80,52,99},new int[]{27,5,64,47,73,88,29,61,88,91,99,44,25,93,77,80,76,95,27,59,98,97,69,99,5,58,7,16,74,43,48,59,4,33,36,75,10,73,60,48,85,35,77,61,26,61,65,30},new int[]{39,84,58,47,4,37,53,41,54,75,98,50,98,36,16,95,85,32,63,45,70,40,92,81,30,76,41,21,86,71,13,56,48,13,36,5,39,5,21,44,87,31,26,28,34,65,75,8},new int[]{8,89,99,81,99,51,90,59,75,96,23,49,29,63,15,86,50,26,51,55,45,89,88,49,62,92,52,78,58,53,63,84,45,43,52,3,12,42,4,87,81,32,52,44,79,1,62,63},new int[]{77,11,44,2,2,81,31,15,15,58,6,90,84,99,95,64,67,21,92,22,97,35,13,77,37,46,9,92,10,26,90,94,25,57,4,36,61,97,1,18,86,32,8,67,81,70,48,90},new int[]{17,69,7,39,49,60,41,58,75,85,89,62,11,55,85,37,20,24,80,36,68,75,94,3,11,42,5,43,75,76,16,78,79,61,67,78,79,61,8,24,66,31,97,35,91,33,31,60},new int[]{25,42,49,77,52,3,53,62,34,91,21,85,24,73,60,10,55,97,7,73,41,39,86,40,58,76,9,12,7,91,32,43,48,95,55,71,39,41,26,61,30,98,89,39,14,40,6,76},new int[]{64,99,34,93,26,89,72,1,31,68,93,46,44,96,88,92,6,70,68,33,83,39,15,42,70,86,53,78,23,9,15,10,17,71,96,22,8,40,90,94,32,95,90,7,13,49,4,97},new int[]{53,17,23,66,81,12,48,28,48,71,54,35,93,21,87,34,50,17,17,1,14,27,15,35,23,32,21,56,52,43,45,38,74,52,28,40,51,99,72,47,82,78,9,16,44,94,38,90},new int[]{52,48,12,76,55,89,94,97,52,99,1,29,41,1,78,43,86,16,93,29,25,83,83,78,71,57,98,19,19,25,13,55,52,95,75,14,28,38,93,88,69,53,20,44,67,57,94,7},new int[]{34,46,56,14,19,41,73,18,96,99,45,82,1,93,51,80,5,20,14,29,96,16,92,18,17,12,87,77,65,70,46,90,32,53,56,69,50,50,92,52,84,42,58,11,90,80,55,66},new int[]{2,35,27,4,13,85,68,1,21,62,1,95,16,32,19,80,37,81,6,97,44,95,55,88,35,16,75,35,57,81,89,9,41,68,53,58,80,86,84,43,65,69,23,32,13,36,52,5},new int[]{11,74,57,15,92,66,10,83,98,58,32,95,13,66,39,33,23,18,86,90,85,5,96,2,40,17,19,7,39,32,70,90,39,2,69,57,20,47,81,20,52,81,17,91,72,17,20,98},new int[]{96,37,13,9,80,60,58,46,62,79,36,48,34,6,44,30,56,94,34,79,76,89,60,3,18,8,45,95,68,5,9,82,8,34,20,27,34,34,12,15,58,59,80,76,10,65,36,39},new int[]{20,10,39,70,21,21,80,89,99,42,40,67,73,18,16,74,33,92,22,28,13,19,81,38,52,70,41,39,13,87,53,61,48,43,31,14,22,19,39,95,61,49,6,36,61,15,81,53},new int[]{68,26,46,53,96,87,73,7,35,56,89,41,58,24,14,4,24,77,76,47,19,60,85,1,87,60,89,88,20,60,57,56,11,54,90,85,79,63,37,33,11,6,12,9,16,41,68,52},new int[]{44,20,66,30,16,72,15,3,31,32,69,93,77,43,50,63,72,42,98,28,49,9,34,49,65,89,80,31,67,12,75,27,60,65,36,96,86,70,2,39,63,46,95,40,10,99,27,22},new int[]{67,2,94,6,87,53,8,87,36,39,72,59,85,60,19,36,71,71,16,48,68,35,3,99,81,31,40,45,49,33,54,69,75,78,7,60,5,5,42,57,94,75,9,32,83,1,49,15},new int[]{23,31,16,78,68,20,21,55,59,71,90,72,43,2,79,11,93,64,19,21,84,89,93,1,20,5,39,77,81,82,19,44,59,71,7,63,79,94,37,63,89,52,52,30,61,22,33,3},new int[]{98,99,44,46,75,2,87,79,39,85,80,76,21,22,67,46,88,94,32,43,27,41,31,99,15,25,99,66,55,92,11,18,14,36,43,12,9,50,43,97,25,60,9,70,12,43,95,87},new int[]{51,61,10,97,97,32,40,18,14,90,39,1,57,62,52,51,35,94,48,63,72,16,85,24,1,66,61,7,17,50,82,31,72,83,95,15,57,99,65,51,18,73,76,94,35,73,36,84},new int[]{22,73,81,80,43,73,95,3,24,5,42,31,49,54,97,53,69,25,48,67,39,98,83,83,55,74,45,83,78,15,95,56,94,80,42,38,95,71,49,94,7,7,47,13,45,25,50,64},new int[]{88,80,68,97,95,56,44,59,2,30,62,54,47,2,56,68,22,87,81,71,73,80,64,87,34,29,71,98,22,64,78,29,90,15,25,66,39,92,91,75,79,11,35,57,95,74,13,27},new int[]{23,99,14,62,52,33,98,58,62,13,77,21,34,36,81,40,1,1,71,59,2,85,35,50,48,62,24,24,79,26,14,52,93,76,88,98,10,34,45,73,51,31,22,19,64,95,6,8},new int[]{20,88,73,46,27,35,76,10,38,80,58,26,3,72,29,45,46,12,91,23,9,15,33,15,24,14,40,73,14,4,89,78,40,11,59,76,77,80,33,3,61,1,54,65,89,53,54,38},new int[]{22,73,56,45,75,2,10,5,88,72,42,34,24,12,52,23,48,69,19,77,35,8,76,85,49,92,76,5,13,54,49,58,15,45,96,72,81,64,54,82,87,4,60,23,8,95,40,13},new int[]{95,49,45,39,82,36,91,66,26,2,33,80,4,55,32,81,61,7,79,83,56,67,67,5,49,20,3,61,23,16,10,64,62,36,79,74,49,67,64,14,84,29,68,52,62,39,54,50},new int[]{75,71,26,55,45,54,26,94,10,44,68,30,12,87,47,72,92,85,25,78,33,42,90,33,45,50,61,14,82,61,26,81,58,4,88,69,5,91,3,24,90,88,42,52,96,54,6,49},new int[]{56,17,62,40,7,94,96,82,92,15,68,71,56,47,5,7,63,28,76,93,25,71,47,20,77,48,95,3,69,77,77,50,60,66,91,75,1,11,13,39,30,7,89,19,80,22,75,68}});
    List<Integer> param1 = new ArrayList<>();
    param1.add(22);
    param1.add(12);
    param1.add(12);
    param1.add(18);
    param1.add(20);
    param1.add(24);
    param1.add(30);
    param1.add(15);
    param1.add(16);
    param1.add(35);
    List<Integer> param2 = new ArrayList<>();
    param2.add(27);
    param2.add(18);
    param2.add(8);
    param2.add(12);
    param2.add(18);
    param2.add(15);
    param2.add(36);
    param2.add(14);
    param2.add(10);
    param2.add(31);

    for(int i =0; i < param0.size(); ++i ){
        for(int j =0; j < param0.get(i).length; ++j ){
            Arrays.sort(param0.get(i)[j]);

            for(int k =0; k < param0.get(i)[j].length; ++k){
                param0.get(i)[j][k]-=50;
            }
        }
    }
    for(int i = 0; i < param0.size(); ++i)
    {
        if(countNegative(param0.get(i),param1.get(i),param2.get(i)) == f_gold(param0.get(i),param1.get(i),param2.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println("#Results:" + n_success + ", " + param0.size());
}
}