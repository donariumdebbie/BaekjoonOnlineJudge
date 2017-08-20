# Completed  2017-08-20

# correct code
from __future__ import division
input_numbers = raw_input()
int_nums = [int(item) for item in input_numbers.split()]
print int_nums[0]/int_nums[1]



# first submitted : correct but runtime error
# import numpy as np
# input_numbers = raw_input()
# int_nums = [int(item) for item in input_numbers.split()]
# print np.true_divide(int_nums[0],int_nums[1])