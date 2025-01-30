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
class REARRANGE_ARRAY_MAXIMUM_MINIMUM_FORM_SET_2_O1_EXTRA_SPACE{
public static void f_gold ( int arr [ ] , int n ) {
  int max_idx = n - 1 , min_idx = 0 ;
  int max_elem = arr [ n - 1 ] + 1 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( i % 2 == 0 ) {
      arr [ i ] += ( arr [ max_idx ] % max_elem ) * max_elem ;
      max_idx -- ;
    }
    else {
      arr [ i ] += ( arr [ min_idx ] % max_elem ) * max_elem ;
      min_idx ++ ;
    }
  }
  for ( int i = 0 ;
  i < n ;
  i ++ ) arr [ i ] = arr [ i ] / max_elem ;
}


//TOFILL

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{1,1,2,3,9,10,14,22,26,28,29,29,30,32,32,32,34,37,39,40,42,42,42,43,45,47,49,52,53,54,56,58,59,68,71,73,76,81,81,83,84,91,94});
    param0.add(new int[]{50,46,6,-57,67,34,-52,26,-93,97,-84,29,15,-63,65,25,-19,92,-38,-28,89,25,61,-34,-70,-80,88,-18,7,52,32,-63,32,-23,-11,46,-12,94,76,-67,-42});
    param0.add(new int[]{0,0,0,0,0,0,1,1,1});
    param0.add(new int[]{15,99,57,69,22,64,41,87,71,56,23,25,91,6,34,63,9,60,49,97,51,60,70,37,31,98,41,62,93,58,14,36,36,79,8,26,36,48,85,28,68,62,80,86,76,80,51});
    param0.add(new int[]{-99,-99,-90,-90,-85,-85,-79,-77,-72,-71,-67,-66,-61,-39,-39,-35,-35,-23,-20,-18,-16,-13,-2,1,5,6,10,24,27,32,33,38,48,67,70,76,82,88});
    param0.add(new int[]{0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0,0,1,0});
    param0.add(new int[]{2,22,32,34,43,66,70,74,94,94});
    param0.add(new int[]{-99,-28,76,-50,41,-85,-47,72,-92,-26,-54,-31,14,47,66,23});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{19,31,26,42,41,23,47,13,89,66,66,16,73,28,77,35,41,77,31,85,32,54,98,72,59});
    List<Integer> param1 = new ArrayList<>();
    param1.add(29);
    param1.add(38);
    param1.add(4);
    param1.add(30);
    param1.add(34);
    param1.add(33);
    param1.add(6);
    param1.add(10);
    param1.add(42);
    param1.add(20);
    List<int [ ]> filled_function_param0 = new ArrayList<>();
    filled_function_param0.add(new int[]{1,1,2,3,9,10,14,22,26,28,29,29,30,32,32,32,34,37,39,40,42,42,42,43,45,47,49,52,53,54,56,58,59,68,71,73,76,81,81,83,84,91,94});
    filled_function_param0.add(new int[]{50,46,6,-57,67,34,-52,26,-93,97,-84,29,15,-63,65,25,-19,92,-38,-28,89,25,61,-34,-70,-80,88,-18,7,52,32,-63,32,-23,-11,46,-12,94,76,-67,-42});
    filled_function_param0.add(new int[]{0,0,0,0,0,0,1,1,1});
    filled_function_param0.add(new int[]{15,99,57,69,22,64,41,87,71,56,23,25,91,6,34,63,9,60,49,97,51,60,70,37,31,98,41,62,93,58,14,36,36,79,8,26,36,48,85,28,68,62,80,86,76,80,51});
    filled_function_param0.add(new int[]{-99,-99,-90,-90,-85,-85,-79,-77,-72,-71,-67,-66,-61,-39,-39,-35,-35,-23,-20,-18,-16,-13,-2,1,5,6,10,24,27,32,33,38,48,67,70,76,82,88});
    filled_function_param0.add(new int[]{0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0,0,1,0});
    filled_function_param0.add(new int[]{2,22,32,34,43,66,70,74,94,94});
    filled_function_param0.add(new int[]{-99,-28,76,-50,41,-85,-47,72,-92,-26,-54,-31,14,47,66,23});
    filled_function_param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    filled_function_param0.add(new int[]{19,31,26,42,41,23,47,13,89,66,66,16,73,28,77,35,41,77,31,85,32,54,98,72,59});
    List<Integer> filled_function_param1 = new ArrayList<>();
    filled_function_param1.add(29);
    filled_function_param1.add(38);
    filled_function_param1.add(4);
    filled_function_param1.add(30);
    filled_function_param1.add(34);
    filled_function_param1.add(33);
    filled_function_param1.add(6);
    filled_function_param1.add(10);
    filled_function_param1.add(42);
    filled_function_param1.add(20);
    for(int i = 0; i < param0.size(); ++i)
    {
        rearrange(filled_function_param0.get(i),filled_function_param1.get(i));
        f_gold(param0.get(i),param1.get(i));
        if(Arrays.equals(param0.get(i), filled_function_param0.get(i)) && param1.get(i) == filled_function_param1.get(i))
        {
            n_success+=1;
        }
    }
    System.out.println("#Results:" + n_success + ", " + param0.size());
}
}