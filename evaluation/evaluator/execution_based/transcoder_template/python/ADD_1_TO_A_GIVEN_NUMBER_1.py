# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( x ) :
    return ( - ( ~ x ) ) ;


#TOFILL

if __name__ == '__main__':
    param = [
    (20,),
    (68,),
    (52,),
    (61,),
    (3,),
    (88,),
    (41,),
    (78,),
    (94,),
    (18,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if addOne(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))