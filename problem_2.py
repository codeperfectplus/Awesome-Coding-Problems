"""
Given an array of integers, return a new array such that each element at index i of the new array is 
the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""
from functools import reduce
from timer import timer


@timer
def main(num_list: list) -> list:
    list_mul = reduce(lambda x, y: x * y, num_list)
    result = [int(list_mul/num) for num in num_list]
    return result


if __name__ == "__main__":
    """ test cases """
    assert main([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert main([3, 2, 1]) == [2, 3, 6]
    assert main([1, 4, 5]) == [20, 5, 4]
    assert main([1, 2, 3, 4, 5, 6]) == [720, 360, 240, 180, 144, 120]
    

