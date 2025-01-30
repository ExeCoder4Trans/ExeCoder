# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( n ) :
    return 1 if ( n == 1 or n == 0 ) else n * f_gold ( n - 1 ) ;


#TOFILL

if __name__ == '__main__':
    param = [
    (84,),
    (41,),
    (5,),
    (38,),
    (79,),
    (80,),
    (64,),
    (62,),
    (24,),
    (12,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if factorial(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))